vlib work

#Include files and compile them
vcom "src/pack_mips.vhd"
vcom "src/my_package.vhd"
vcom "src/alu.vhd"
vcom "src/testbench.vhd"

# Start simulation
vsim -vopt work.testbench

# Draw waves

# Run simulation
run 300000000 ns

quit -f
