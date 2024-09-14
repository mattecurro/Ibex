import subprocess
import fileinput
import sys

# Definire i comandi
commands_small = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py small fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]

commands_opentitan = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py opentitan fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]

commands_maxperf = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py maxperf fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]

commands_maxperf_with_cache = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py maxperf_with_cache fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]


commands_maxperf_pmp_bmbalanced = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py maxperf-pmp-bmbalanced fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]

commands_maxperf_pmp_bmfull_icache = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py maxperf-pmp-bmfull-icache fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]

commands_maxperf_pmp_bmfull = [
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "sudo fusesoc --cores-root=. run --target=sim --setup --build lowrisc:ibex:ibex_simple_system `./util/ibex_config.py maxperf-pmp-bmfull fusesoc_opts`",
    "make -C ./examples/sw/benchmarks/coremark/ clean",
    "make -C ./examples/sw/benchmarks/coremark/",
    "build/lowrisc_ibex_ibex_simple_system_0/sim-verilator/Vibex_simple_system --meminit=ram,examples/sw/benchmarks/coremark/coremark.elf"
]




# Function to run a shell script
def run_shell_script(script_path, *args):
    command = [script_path] + list(args)
    process = subprocess.run(command, check=True)
    if process.returncode != 0:
        print(f"Error during execution of script: {script_path} with arguments: {args}")
    else:
        print(f"Script executed successfully: {script_path} with arguments: {args}")

# Function to update a variable in a .cc file
def update_cc_file(filename, variable_name, new_value):
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            if line.strip().startswith(f"#define {variable_name}"):
                print(f"#define {variable_name} {new_value}")
            else:
                print(line, end='')


# Function to update a variable in a .sv file
def update_sv_file(filename, variable_name, new_value):
    found = False
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            if line.strip().startswith(f"parameter int unsigned {variable_name}"):
                print(f"  parameter int unsigned {variable_name} = {new_value};")
                found = True
            else:
                print(line, end='')


# Path to .sv file
sv_file_path = './rtl/ibex_pkg.sv'

# Path to .cc file
cc_file_path = './examples/simple_system/ibex_simple_system.cc'


#1,42
# Eseguire i comandi 5 volte
for i in range(2):
    print(f"Esecuzione iterazione {i + 1}...")
    
    # Update the .cc file variable
    update_cc_file(cc_file_path, 'REAL_DATA_SIZE_STR', 1000 + i * 209000)
    
    
    run_shell_script('./update_total_data_size_bash.sh', './examples/sw/benchmarks/coremark/Makefile', str(1000 + i * 209000))

    
    update_cc_file(cc_file_path, 'TYPOLOGY', '"small"')
    
    
    for command in commands_small:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")
    	
    	
    
    update_cc_file(cc_file_path, 'TYPOLOGY', '"opentitan_4096"')   	
    update_sv_file(sv_file_path, 'IC_SIZE_BYTES', 4096)

    
    for command in commands_opentitan:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")

    
    update_cc_file(cc_file_path, 'TYPOLOGY', '"opentitan_8192"')   	
  
    update_sv_file(sv_file_path, 'IC_SIZE_BYTES', 8192)
    
    for command in commands_opentitan:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")

 
    update_sv_file(sv_file_path, 'IC_SIZE_BYTES', 4096)
       	    
    update_cc_file(cc_file_path, 'TYPOLOGY', '"maxperf"')   	

    
    for command in commands_maxperf:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")


    update_cc_file(cc_file_path, 'TYPOLOGY', '"maxperf_with_cache_4096"')   	

    
    for command in commands_maxperf_with_cache:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")




    update_sv_file(sv_file_path, 'IC_SIZE_BYTES', 8192)
       	    
    update_cc_file(cc_file_path, 'TYPOLOGY', '"maxperf_with_cache_8192"')   	

    
    for command in commands_maxperf_with_cache:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")


    update_sv_file(sv_file_path, 'IC_SIZE_BYTES', 4096)

    update_cc_file(cc_file_path, 'TYPOLOGY', '"maxperf-pmp-bmfull"')   	

    
    for command in commands_maxperf_pmp_bmfull:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")


    update_cc_file(cc_file_path, 'TYPOLOGY', '"maxperf-pmp-bmfull-icache"')   	

    
    for command in commands_maxperf_pmp_bmfull_icache:
        process = subprocess.run(command, shell=True, check=True)
        if process.returncode != 0:
            print(f"Errore durante l'esecuzione del comando: {command}")
        else:
            print(f"Comando eseguito con successo: {command}")



    update_cc_file(cc_file_path, 'REAL_DATA_SIZE_STR', 1000 + i * 1000)
 

print("Exe completed.")

