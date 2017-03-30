# Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran

import sys, os
# in this dictionary we describe untestable points between related functions!

# use the function number in the table file!
# "10000000" means that only the most significant bit is provable to be testable
# "01111111" the most significant bit is not testable
related_functions = { "10_11" : "10000000",  	# SHR, ASR
					  "11_10" : "10000000",		# ASR, SHR
					  "12_13" : "11111110",		# INC, DEC
					  "13_12" : "11111110",		# DEC, INC
					  "4_11"  : "01111111",		# CMP, ASR
					  "11_4"  : "01111111",		# ASR, CMP
					  "2_7"   : "11111110",		# ADD, XOR
					  "7_2"   : "11111110",		# XOR, ADD
					  "3_7"   : "11111110",		# SUB, XOR
					  "7_3"   : "11111110",		# XOR, SUB
					  "3_2"   : "11111110",		# SUB, ADD
					  "2_3"   : "11111110",		# ADD, SUB
					  "6_2"   : "11111110",		# OR, ADD
					  "6_3"   : "11111110",		# OR, SUB
					  "6_11"  : "01111111",		# OR, ASR
					  "11_14"  : "01111111",	# ASR, RLC
					  "11_15"  : "01111111",	# ASR, RRC
					  "14_11"  : "01111111",	# ASR, RLC
					  "15_11"  : "01111111",	# ASR, RRC
					  "11_5"  : "01111111",		# ASR, ANd
}

pre_determinde_patterns = {
							"F1" : [1, 2, 6, 4, 7],
							"F2" : [1, 2, 3, 4, 7, 9, 13, 11, 16], 
							"F3" : [2, 3, 4, 7, 8, 6, 15, 10, 11, 12], 
							"F4" : [1, 2, 3, 4, 5, 6, 10, 15, 9, 11, 14, 16, 20], 
							"F5" : [1, 2, 3, 4, 5, 6, 10, 7], 
							"F6" : [2, 3, 5, 8, 11, 15, 19, 12, 14], 
							"F7" : [1, 2, 3, 4, 7, 11, 12, 5, 15, 14], 
							"F8" : [1, 2, 3, 4, 7, 10, 12, 5, 8], 
							"F9" : [1, 2, 3, 4, 5, 11, 6, 10, 12, 16, 13], 
							"F10" : [1, 2, 3, 4, 8, 19, 12, 9, 13, 5, 7, 6], 
							"F11" : [2, 3, 4, 8, 19, 1, 12, 9, 13, 5, 7, 6], 
							"F12" : [1, 3, 4, 5, 7, 10, 2, 6, 15, 9, 14], 
							"F13" : [1, 3, 4, 5, 6, 10, 2, 15, 9, 20, 12, 14], 
							"F14" : [1, 2, 3, 4, 5, 6, 10, 15, 9, 11, 14, 16, 20], 
							"F15" : [1, 2, 3, 4, 5, 6, 10, 15, 9, 11, 14, 16, 20], 
							"F16" : [1, 2, 3, 4, 7, 6], 
} 

generated_files_folder = "../generated_files"
data_width  = 8

def run_scanning_optimization(scanning_test_f1, function_dict, func_id_1, debug, verbose, list_of_necessary_patterns):
	if scanning_test_f1.count("1") != len(scanning_test_f1):
		scanning_dict = find_most_signifacant_scanning(function_dict, func_id_1, scanning_test_f1, debug, verbose)
		max_coverable_scanning = max(scanning_dict.keys())
		if verbose:
			print "number of missing ones:", scanning_test_f1.count("0")
			print "max ones that can be covered:", max_coverable_scanning
		if scanning_test_f1.count("0") == max_coverable_scanning:
			if scanning_dict[max_coverable_scanning][0] not in list_of_necessary_patterns:
				if verbose:
					print "adding pattern", scanning_dict[max_coverable_scanning][0], "to the list of solutions for scanning test!"
				list_of_necessary_patterns.append(scanning_dict[max_coverable_scanning][0])
				scanning_test_f1 = format(int(scanning_test_f1, 2) | int(function_dict[scanning_dict[max_coverable_scanning][0]][func_id_1], 2), 'b').zfill(data_width)
			if verbose:
				print "All ones!"
		elif max_coverable_scanning == 0:
			if verbose:
				print "scanning test can not be improved!"
		else:
			while max_coverable_scanning != 0:
				if scanning_dict[max_coverable_scanning][0] not in list_of_necessary_patterns:
					if verbose:
						print "adding pattern", scanning_dict[max_coverable_scanning][0], "to the list of solutions!"
					list_of_necessary_patterns.append(scanning_dict[max_coverable_scanning][0])
					scanning_test_f1 = format(int(scanning_test_f1, 2) | int(function_dict[scanning_dict[max_coverable_scanning][0]][func_id_1], 2), 'b').zfill(data_width)
					scanning_dict = find_most_signifacant_scanning(function_dict, func_id_1, scanning_test_f1, debug, verbose)
					max_coverable_scanning = max(scanning_dict.keys())
					if scanning_test_f1.count("0") == max_coverable_scanning:
						if scanning_dict[max_coverable_scanning][0] not in list_of_necessary_patterns:
							if verbose:
								print "adding pattern", scanning_dict[max_coverable_scanning][0], "to the list of solutions scanning test!"
							list_of_necessary_patterns.append(scanning_dict[max_coverable_scanning][0])
							scanning_test_f1 = format(int(scanning_test_f1, 2) | int(function_dict[scanning_dict[max_coverable_scanning][0]][func_id_1], 2), 'b').zfill(data_width)
						if verbose:
							print "All ones!"
						break
	return scanning_test_f1, list_of_necessary_patterns

	

def final_un_used_pattern(number_of_patterns, final_set_of_patterns):
	"""
	takes the number of patterns and list of final set of patterns and returns a list of un-used 
	patterns!
	number_of_patterns: integer: number of patterns in the input pattern file!
	final_set_of_patterns:  list of integers: list containing all the patterns chosen by the algorithm!
	"""
	final_unused_patterns = []
	for item in range(1, number_of_patterns+1):
		if item not in final_set_of_patterns:
			final_unused_patterns.append(item)

	return final_unused_patterns


def parse_input_pattern_file(input_file_name):
	function_dict = {}
	line_counter = 0
	with open(input_file_name) as f:
		for line in f:
			if line != "":
				line_counter += 1
				list_of_functions =  line.split(" ")
				list_of_functions[len(list_of_functions)-1] = list_of_functions[len(list_of_functions)-1][:-2]
				function_dict[line_counter] = list_of_functions
	return function_dict


def generate_folders(generated_files_folder):
	"""
	This function checkes if the generated_files_folder exists, if so, it removes all the files in it
	if not, it generates the folder
	generated_files_folder: string : path to the generated files folder
	returns: None
	"""
	if os.path.exists(generated_files_folder):
		file_list = [file for file in os.listdir(generated_files_folder)]
		for file in file_list:
			os.remove(generated_files_folder+'/'+file)
	else:
	    os.mkdir(generated_files_folder)
	return None


def make_table_header(table_file, len_of_list):
	"""
	writes the header for the table files
	table_file: table file, should be open!
	len_of_list: represents the number of functions in the experiment
	returns: None
	"""
	string =  '%10s' %(" ")
	for function in range(1, len_of_list-1):
		string += "\t"+'%8s' %("f_"+str(function)) # -1 to march the number of functions for readability
	table_file.write(string+"\n")
	string = '%10s' %(" ")+ "\t" + "------------"*(len_of_list-2)
	table_file.write(string+"\n")
	return None

def find_most_signifacant_scanning(function_dict, function_id_1, current_covered, debug, verbose):
	list_of_ones_in_ands = {}

	not_covered = format(int("1"*data_width, 2) ^ int(str(current_covered), 2), 'b').zfill(data_width)		# inverse of the current_covered! to find what has not been covered so far
	if verbose:
		print "\tcurrently covered:", current_covered
		print "\tcurrently not covered:", not_covered
	for i in sorted(function_dict.keys()):
		new_ones =  format(int(not_covered, 2) & int(function_dict[i][function_id_1], 2), 'b').zfill(data_width) 
		if new_ones.count("1") in list_of_ones_in_ands.keys():
			list_of_ones_in_ands[new_ones.count("1")].append(i)
		else:
			list_of_ones_in_ands[new_ones.count("1")] = [i]
	return list_of_ones_in_ands


def find_most_signifacant_conformity(function_dict, function_id_1, function_id_2, list_of_used_patterns, list_of_excluded_patterns, current_covered, debug, verbose):
	"""
	takes the current state of the covered nodes, i.e. current_covered as a string of binary number 
	and searches in the patterns in list_of_used_patterns and returns a dictionary with number of 
	ones as keys and list pattern numbers as value.
	
	Example:
			current_covered:    10011101 
	patterns in list_of_used_patterns:
	
			pattern no |final and_op for pattern
			-----------|------------------------
				1	   |		00001111
				2	   |		10101010
				3	   |		11110000
				4	   |		01010101
				5	   |		00110011

	list_of_ones_in_ands = {1: [1, 4], 2:[2, 3, 5]}	
	"""
	list_of_ones_in_ands = {}
	or_op = "0"*data_width
	not_covered = format(int("1"*data_width, 2) ^ int(str(current_covered), 2), 'b').zfill(data_width)		# inverse of the current_covered! to find what has not been covered so far
	if verbose:
		print "\tcurrently covered:", current_covered
		print "\tcurrently not covered:", not_covered
	if debug:
		print "\tfinding the patterns with most uncovered ones!"
		print "\t\tline\top1\t\top2\t\tfunc_1 \t\t func_2\t\txor(1,2)\tand(1,xor)\tor(prev_or,and)"
		print "\t\t"+"------------------------------------------"*3
	for i in sorted(function_dict.keys()):
		if i in list_of_used_patterns:
			if i not in list_of_excluded_patterns:
				xor_op = format(int(function_dict[i][function_id_1], 2) ^ int(function_dict[i][function_id_2], 2), 'b').zfill(data_width)
				and_op = format(int(function_dict[i][function_id_2], 2) & int(xor_op, 2), 'b').zfill(data_width)
				new_ones =  format(int(not_covered, 2) & int(and_op, 2), 'b').zfill(data_width) 
				if new_ones.count("1") in list_of_ones_in_ands.keys():
					list_of_ones_in_ands[new_ones.count("1")].append(i)
				else:
					list_of_ones_in_ands[new_ones.count("1")] = [i]
				or_op = format(int(or_op, 2) | int(and_op, 2), 'b').zfill(data_width)		
				if debug:		
					print "\t\t"+str(i)+"\t", function_dict[i][0],"\t", function_dict[i][1],"\t", function_dict[i][function_id_1], "\t", function_dict[i][function_id_2], "\t", xor_op, "\t"+str(and_op), "\t"+str(or_op)
	return list_of_ones_in_ands


def print_results(final_set_of_patterns, final_unsed_patterns, verbose):
	print "------------------------------------------"*3
	print "|"+"                                         "*3+" |"
	print "|"+"                                         "+"                RESULTS                  "+"                                         "+" |"
	print "|"+"                                         "*3+" |"
	print "------------------------------------------"*3
	print "final list of patterns used in the experiment:"
	print "number of patterns used:", len(final_set_of_patterns)
	print sorted(final_set_of_patterns)
	if verbose:
		print "------------------------------------------"*3
		print "final list of patterns NOT used in the experiment:"
		print "number of patterns NOT used:", len(final_unsed_patterns)
		print sorted(final_unsed_patterns)
	return None

def print_fault_coverage(number_of_lines, number_of_ones_in_experiments, number_of_zeros_in_experiments):
	print "------------------------------------------"*3
	print "|"+"                                         "+"             FAULT COVERAGE              "+"                                         "+" |"
	print "------------------------------------------"*3
	print "number of patterns:", number_of_lines
	print "number of faults covered:", number_of_ones_in_experiments
	print "number of faults not covered:" , number_of_zeros_in_experiments
	print "NOTE: fault coverage =  (number of faults covered)/(number of faults covered + number of faults not covered)"
	print "fault coverage :", "{:1.2f}".format(100*float(number_of_ones_in_experiments)/(number_of_ones_in_experiments+number_of_zeros_in_experiments)),"%"
	return None

def report_usefull_patterns_per_round(used_dic, len_of_list):
	print "-----------------------------------------------------"
	print "function pair", "\t", "\t", '%100s' % "usefull patterns","\t",'%10s' % "test length"
	print "-------------", "\t", "\t", '%100s' % "----------------","\t",'%10s' % "----------------"
	counter = 1
	for item in sorted(used_dic.keys()):
		print '%10s' %str(int(item.split("_")[0])-1)+"_"+str(int(item.split("_")[1])-1), "\t",'%100s' %used_dic[item], "\t",'%10s' %len(used_dic[item])
		counter += 1
		if counter == len_of_list-2:
			print "------------------------------------------------------------"*2
			counter = 1

def parse_program_arg(arguments, generated_files_folder):
	global data_width
	if "--help" in arguments[1:] or len(arguments[1:]) == 0:
		print "---------------------------------------------------------------------------"
		print "\n     Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran \n"
		print "This program optimizes test patterns generation between different functions"
		print "program arguments:"
		print "-i [file name]: spcifies the path to the input file" 
		print "-ot [file name]: spcifies the path to the generated table file" 
		print "-ost [file name]: spcifies the path to the generated table file for scanning test" 
		print "-op [file name]: spcifies the path to the generated patterns file" 
		print "-rfr: redundant function reduction, if used, will use the table in package file to ingore the redundency" 
		print "-v: makes it more verbose" 
		print "-dw [data width]: data width of the patterns, default is 8" 
		print "-debug: enables debug printing"
		print "---------------------------------------------------------------------------"
		sys.exit()

	if "-i" in arguments[1:]:
		input_file_name = arguments[arguments.index('-i') + 1]

	if "-v" in arguments[1:]:
		verbose = True
	else:
		verbose = False

	if "-debug" in arguments[1:]:
		debug = True
	else:
		debug = False

	if "-ot" in arguments[1:]:
		output_table_file_name = generated_files_folder + "/" + arguments[arguments.index('-ot') + 1]
	else:
		output_table_file_name = generated_files_folder + "/" + "table.txt"
		
	if "-op" in arguments[1:]:
		output_patterns_file_name = generated_files_folder + "/" + arguments[arguments.index('-op') + 1]
	else:
		output_patterns_file_name = generated_files_folder + "/" + "patterns.txt"

	if "-ost" in arguments[1:]:
		scanning_table_file_name = generated_files_folder + "/" + arguments[arguments.index('-ost') + 1]
	else:
		scanning_table_file_name = generated_files_folder + "/" + "scanning_table.txt"

	if "-rfr" in arguments[1:]:
		redundant_function_reduction = True
	else:
		redundant_function_reduction = False

	if "-dw" in arguments[1:]:
		data_width = int(arguments[arguments.index('-dw') + 1])
	else:
		data_width = 8

	return input_file_name, verbose, debug, output_table_file_name, output_patterns_file_name, scanning_table_file_name, redundant_function_reduction