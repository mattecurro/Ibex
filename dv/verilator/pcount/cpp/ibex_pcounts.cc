// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

#include <numeric>
#include <sstream>
#include <string>
#include <vector>

#include <svdpi.h>

extern "C" {
extern unsigned int mhpmcounter_num();
extern unsigned long long mhpmcounter_get(int index);
}

#include "ibex_pcounts.h"

// see mhpmcounter_incr signals in rtl/ibex_cs_registers.sv for details

const std::vector<std::string> ibex_counter_names = {
    "Cycles",
    "NONE",
    "Instructions Retired",
    "LSU Busy",
    "Fetch Wait",
    "Loads",
    "Stores",
    "Jumps",
    "Conditional Branches",
    "Taken Conditional Branches",
    "Compressed Instructions",
    "Multiply Wait",
    "Divide Wait"};

static bool has_hpm_counter(int index) {
  // The "cycles" and "instructions retired" counters are special and always
  // exist.
  if (index == 0 || index == 2)
    return true;

  // The "NONE" counter is a placeholder. The space reserves an index that was
  // once the "MTIME" CSR, but now is unused. Return false: there's no real HPM
  // counter at index 1.
  if (index == 1)
    return false;
 
  // Otherwise, a counter exists if the index is strictly less than
  // the MHPMCounterNum parameter that got passed to the
  // ibex_cs_registers module.
  return index < mhpmcounter_num();
}

std::string ibex_pcount_string(bool csv) {
  char separator = csv ? ',' : ':';
  std::string::size_type longest_name_length;

  if (!csv) {
    longest_name_length = 0;
    for (int i = 0; i < ibex_counter_names.size(); ++i) {
      if (has_hpm_counter(i)) {
        longest_name_length =
            std::max(longest_name_length, ibex_counter_names[i].length());
      }
    }

    // Add 1 to always get at least once space after the separator
    longest_name_length++;
  }

  std::stringstream pcount_ss;

  for (int i = 0; i < ibex_counter_names.size(); ++i) {
    if (!has_hpm_counter(i))
      continue;

    if(i != 10 && i != 11 && i != 12)
      pcount_ss << ibex_counter_names[i] << separator;

    if (!csv) {
      int padding = longest_name_length - ibex_counter_names[i].length();

      for (int j = 0; j < padding; ++j)
        pcount_ss << ' ';
    }


    if(i != 10 && i != 11 && i != 12)
      pcount_ss << mhpmcounter_get(i) << std::endl;
  }

  // Recupera i valori dei contatori
  uint64_t instructions_retired = mhpmcounter_get(2);
  uint64_t cycles = mhpmcounter_get(0);
  uint64_t fetch_wait = mhpmcounter_get(4);
  uint64_t conditional_branches = mhpmcounter_get(8);
  uint64_t taken_conditional_branches = mhpmcounter_get(9);


  // Calcola il rapporto come valore in virgola mobile
  double i_c_ratio = static_cast<double>(instructions_retired) / static_cast<double>(cycles);
  double f_i_ratio = static_cast<double>(fetch_wait) / static_cast<double>(instructions_retired);
  double t_c_ratio = static_cast<double>(taken_conditional_branches) / static_cast<double>(conditional_branches);

  pcount_ss << "Instructions Retired / Cycles" << separator;
  // Aggiungi il calcolo formattato
  pcount_ss << i_c_ratio << std::endl;

  pcount_ss << "Fetch Wait / Instruction Retired" << separator;
  pcount_ss << f_i_ratio << std::endl;


  pcount_ss << "Taken Conditional Branches / Conditional Branches" << separator;
  pcount_ss << t_c_ratio << std::endl;

  pcount_ss << "\n\n\n\n\n" << std::endl;
 
  return pcount_ss.str();
}
