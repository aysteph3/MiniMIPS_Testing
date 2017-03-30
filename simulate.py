import os
from randomGenrate import *
#import randomGenrate
from  merge import *

def main():

	if os.path.exists("sim_generated_file"):
		files = [file for file in os.listdir("sim_generated_file")]
		for file in files:
			os.remove("sim_generated_file"+"/"+file)
	else:
		os.mkdir("sim_generated_file")

	generate_pattern_t(test_l,bit_l)
	
	os.system("vsim -do " + "simulate.do")
	filename = "sim_generated_file/out.txt"
	mergefile(filename)

if __name__== "__main__":
  main()