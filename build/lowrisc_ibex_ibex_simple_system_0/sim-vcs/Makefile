all: lowrisc_ibex_ibex_simple_system_0

lowrisc_ibex_ibex_simple_system_0: lowrisc_ibex_ibex_simple_system_0.scr
	vcs -full64 -top ibex_simple_system -f lowrisc_ibex_ibex_simple_system_0.scr -o $@  -CFLAGS -I../../src/lowrisc_dv_crypto_prince_ref_0.1 -CFLAGS -I../../src/lowrisc_dv_secded_enc_0 -CFLAGS -I../../src/lowrisc_dv_scramble_model_0 -CFLAGS -I../../src/lowrisc_dv_verilator_memutil_dpi_0/cpp -lelf -CFLAGS -I../../src/lowrisc_dv_verilator_memutil_dpi_scrambled_0/cpp -lelf -xlrm uniq_prior_final -debug_access+r -sverilog
run: lowrisc_ibex_ibex_simple_system_0
	./lowrisc_ibex_ibex_simple_system_0 -l vcs.log 
clean:
	$(RM) lowrisc_ibex_ibex_simple_system_0
