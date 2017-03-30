import random
import os

"""fixes the number of random number generated each time executed. 
If removed random number changes each time"""
random.seed(10110010011010101100101100101001) 
# function that generates random binary number
def randbin2(d): 
    mx = (2 ** d) - 1
    #for counter in range(1,lenght+1):
    while True:
        b = bin(random.randint(0, mx)) 
        return b[2:].rjust(d, '0') 
        
if os.path.exists("sim_input"):
	files = [file for file in os.listdir("sim_input")]
	for file in files:
		os.remove("sim_input"+"/"+file)
else:
	os.mkdir("sim_input")

      
filename = "sim_input/input.txt"  # input data in format needed by simulation
filename2 = "sim_input/hex_input.txt"
filename3 = "sim_input/inputclone.txt" # clone of input with patterns separated for clarity

target = open(filename, 'w')
target2 = open(filename2, 'w')
target3 = open(filename3, 'w')

test_l = raw_input("test length: ") 
bit_l = raw_input("bit length: ") 

"""method to generate random test patterns. 
where pl is pattern length and bl is bit length""" 
def generate_pattern(pl, bl):
	#print "Input A"
	target.write("Input A\n")
	for counter in range(1,int(pl)+1):      
		ina = randbin2(int(bl))
		#print ina
		target.write(ina)
		target.write("\n")
    	
	#print "Input B"
	target.write("\nInput B\n")
	for counter in range(1,int(pl)+1):      
		inb = randbin2(int(bl))
		#print inb
		target.write(inb)
		target.write("\n")

	target.close()		

# methods generate test patterns in binary and hexadecimal for 2 operands in tabular form
def generate_pattern_t(pl, bl):
	#target.write("Input A"+ "					"+"Input B \n")
	#target2.write("Input A"+ "		"+"Input B \n")
	for counter in range(1,int(pl)+1):      
		ina = randbin2(int(bl)) # call function that generates random binary numbers
		inb = randbin2(int(bl)) # call function that generates random binary numbers
		
		inah = hex(int(ina,2)) # convert binary to hex
		inbh = hex(int(inb,2)) # convert binary to hex
	
		target3.write(ina + "	"+ inb) # format readable. same as input file but readable
		target.write(ina + ""+ inb) #format of data needed for simulation
		target2.write(inah + "	"+ inbh)
		
		target.write("\n")
		target2.write("\n")
		target3.write("\n")

	#target.write("\n")
	#target.write("\n")  # just for simulation
	target.close()
	target2.close()
	target3.close()
	print "test pattern generated"
	
	
	# commented out as not needed for current experiment. The file will be read during simulation
'''def readingF(filen):
	with open(filen,"r") as f:
		text = f.readlines()
		#print len(text)
	for line in text:
		#a, b = map(int, line.split("\t"))  # this casts the values of a and b to integer
		c,d = line.split("\t") # type casting is not done. values of c and d are string
		#print line
		print c
		print d''' 
		
#test call on generate pattern method
#generate_pattern(50,32)

#test call on generate pattern method in tabular form
#generate_pattern_t(test_l,bit_l)
#readingF(filename)

		