import os
from randomGenrate import *
#import randomGenrate
from  merge import *

def main():

	if os.path.exists("generated_file"):
		files = [file for file in os.listdir("generated_file")]
		for file in files:
			os.remove("generated_file"+"/"+file)
	else:
		os.mkdir("generated_file")

	generate_pattern_t(test_l,bit_l)
	
	os.system("vsim -do " + "simulate.do")
	filename = "generated_file/out.txt"
	mergefile(filename)

if __name__== "__main__":
  main()