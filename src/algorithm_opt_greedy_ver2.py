# Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran
# for each new function we start from empty set!
import Logger
import sys
import copy
import itertools
import time
import package

package.generate_folders(package.generated_files_folder)
sys.stdout = Logger.Logger(package.generated_files_folder)

if "-sp" in sys.argv[1:]:
	saf_output_patterns_file_name= package.generated_files_folder + "/" +"SAF"+ sys.argv[sys.argv.index('-sp') + 1]
else:
	saf_output_patterns_file_name= package.generated_files_folder + "/" + "SAFpatterns.txt"

def check_if_sufficient(function_dict, function_id_1, function_id_2, list_patterns, debug, verbose):
	or_op = "0"*package.data_width
	if debug:
		print "\t--------------------"
		print "\tchecking if sufficient number of ones reached!"
		print "\t\tline\top1\t\top2\t\tfunc_1 \t\t func_2\t\txor(1,2)\tand(1,xor)\tor(prev_or,and)"
		print "\t\t"+"------------------------------------------"*3
	for i in list_patterns:
		xor_op = format(int(function_dict[i][function_id_1], 2) ^ int(function_dict[i][function_id_2], 2), 'b').zfill(package.data_width)
		and_op = format(int(function_dict[i][function_id_2], 2) & int(xor_op, 2), 'b').zfill(package.data_width)
		or_op = format(int(or_op, 2) | int(and_op, 2), 'b').zfill(package.data_width)
		if debug:
			print "\t\t"+str(i)+"\t", function_dict[i][0],"\t", function_dict[i][1],"\t", function_dict[i][function_id_1], "\t", function_dict[i][function_id_2], "\t", xor_op, "\t"+str(and_op), "\t"+str(or_op)
	if or_op == "1"*package.data_width:
		if verbose:
			print "\tbingo! all ones!"
		return or_op
	else:
		if debug and verbose:
			print "\tdidnt reach all ones!"
		return or_op

input_file_name, verbose, debug, output_table_file_name, output_patterns_file_name, scanning_table_file_name, redundant_function_reduction = package.parse_program_arg(sys.argv, package.generated_files_folder)

data_width = package.data_width
print "data_width:", data_width

start_time = time.time()

function_dict = copy.deepcopy(package.parse_input_pattern_file(input_file_name))
len_of_list = len(function_dict[function_dict.keys()[0]])
number_of_lines = len(function_dict.keys())

try:
	table_file = open(output_table_file_name, 'w')
	scanning_table_file = open(scanning_table_file_name, 'w')
	test_patterns_file = open(output_patterns_file_name, 'w')
	saf_test_patterns_file = open(saf_output_patterns_file_name, 'w')
except IOError:
    print "Could not open input pattern file, test pattern file, conformity or scanning table file!"
    sys.exit()


if package.test_subset:
	function_list = []
	for item in package.test_only_list:
		function_list.append(item+1)
else:
	function_list = range(2, len_of_list)

package.make_table_header(table_file, function_list)
package.make_table_header(scanning_table_file, function_list)

number_of_ones_in_experiments = 0
number_of_zeros_in_experiments = 0
used_dic = {}
final_set_of_patterns = []
overal_test_length = 0
for func_id_1 in function_list:
	current_set_of_patterns = []
	string =  '%10s' %("f_"+str(func_id_1-1)+"|") 			# -1 to march the number of functions for readability
	scanning_string =  '%10s' %("f_"+str(func_id_1-1)+"|") 	# -1 to march the number of functions for readability
	scanning_test_f1 = "0"*data_width
	for func_id_2 in function_list:
		if func_id_1 != func_id_2:
			scanning_test_f1_f2 = "0"*data_width
			list_of_used_patterns =  range(1, number_of_lines+1)
			if verbose:
				print "------------------------------------------"*3
				print "function 1: ", func_id_1-1, "function 2:", func_id_2-1
				print "------------------------------------------"*3

			counter = 0
			list_of_excluded_patterns = copy.deepcopy(current_set_of_patterns)
			break_the_loop = False
			best_solution = []
			best_value = 0

			sufficient =  check_if_sufficient(function_dict, func_id_1, func_id_2, list_of_excluded_patterns, debug, verbose)

			while(counter < number_of_lines):
				list_of_ones_in_ands = package.find_most_signifacant_conformity(function_dict, func_id_1, func_id_2, list_of_used_patterns,
																				list_of_excluded_patterns, sufficient, debug, verbose)
			 	if len(list_of_ones_in_ands.keys())>0:
			 		if verbose:
					 	print "\tmax number of ones:", max(list_of_ones_in_ands.keys())

				 	if max(list_of_ones_in_ands.keys()) == 0:
				 		break
				 	list_of_best_patterns = list_of_ones_in_ands[max(list_of_ones_in_ands.keys())]
				 	if verbose:
					 	print "\tbest patterns in this round:", list_of_best_patterns
					for item in list_of_best_patterns:
						if type(item) == int:
							item = [item]
						if verbose:
							print "\t----------------------"
							print "\ttrying combination: ", list_of_excluded_patterns+list(item)

						sufficient =  check_if_sufficient(function_dict, func_id_1, func_id_2, list_of_excluded_patterns+list(item), debug, verbose)
						if sufficient.count("1") == len(sufficient):
						 	best_solution = copy.deepcopy(list_of_excluded_patterns+list(item))
						 	if verbose:
							 	print "\twe got it!"
						 	break_the_loop = True
						 	break
						else:
							if verbose:
								print "\tnew number of ones :", sufficient.count("1"), "\t\tprevious value:", best_value
							if sufficient.count("1") > best_value:
								if verbose:
									print "\tfound a better solution!"
						 		list_of_excluded_patterns += list(item)
						 		best_solution = copy.deepcopy(list_of_excluded_patterns)
						 		best_value = sufficient.count("1")

						 		break
						if break_the_loop:
							break
					if break_the_loop:
							break
					counter += 1
				else:
					break
				if verbose:
					print "\t------------------------------------------------------------------"
			if verbose:
				print "best conformity solution for func ", func_id_1-1, " and func ", func_id_2-1, ": ", sufficient, best_solution

			if verbose:
				print "------------------------------"

			for final_pattern in best_solution:
				if final_pattern not in current_set_of_patterns:
					current_set_of_patterns.append(final_pattern)

			string += "\t"+str(sufficient)

			for scan_pattern in best_solution:
				scanning_test_f1_f2 = format(int(scanning_test_f1_f2, 2) | int(function_dict[scan_pattern][func_id_1], 2), 'b').zfill(data_width)

			if redundant_function_reduction:
				if  (str(func_id_1-1)+"_"+str(func_id_2-1) in package.related_functions.keys()):
					number_of_zeros_in_experiments  += sufficient.count("0") - package.related_functions[str(func_id_1-1)+"_"+str(func_id_2-1)].count("0")
				elif (str(func_id_1-1)+"_*" in package.related_functions.keys()):
					number_of_zeros_in_experiments  += sufficient.count("0") - package.related_functions[str(func_id_1-1)+"_*"].count("0")
				elif ("*_"+str(func_id_2-1) in package.related_functions.keys()):
					number_of_zeros_in_experiments  += sufficient.count("0") - package.related_functions["*_"+str(func_id_2-1)].count("0")
				else:
					number_of_zeros_in_experiments  += sufficient.count("0")
			else:
				number_of_zeros_in_experiments  += sufficient.count("0")
			number_of_ones_in_experiments  += sufficient.count("1")

			used_dic['{0:03}'.format(func_id_1)+"_"+'{0:03}'.format(func_id_2)] = copy.deepcopy(current_set_of_patterns)
		else:
			scanning_test_f1_f2 = "0"*data_width
			string += "\t"+"x"*data_width

		scanning_test_f1 =  format(int(scanning_test_f1, 2) | int(scanning_test_f1_f2, 2), 'b').zfill(data_width)
		scanning_string += "\t"+str(scanning_test_f1_f2)

	#-------------------------------------------------------------------------------
	#	This part fixes the scanning test results for the current function pair
	#-------------------------------------------------------------------------------
	scanning_test_f1, best_solution = package.run_scanning_optimization(scanning_test_f1, function_dict, func_id_1, debug, verbose, best_solution)
	scanning_string += "\t"+str(scanning_test_f1)
	scanning_table_file.write(scanning_string+"\n")
	table_file.write(string+"\n")
	for k in current_set_of_patterns:
		if k not in final_set_of_patterns:
			final_set_of_patterns.append(k)

	opcode = "{0:04b}".format((func_id_1-2))
	for j in current_set_of_patterns:
		saf_test_patterns_file.write(function_dict[j][0]+function_dict[j][1]+opcode+"\n")
	#overal_test_length +=   len(list_of_necessary_patterns)

print "reporting test length for functions:"
for func_id_1 in range(2, len_of_list):
	max_lenght = 0
	for item in used_dic.keys():
		if int(item.split("_")[0]) == func_id_1:
			if len(used_dic[item])>max_lenght:
				max_lenght = len(used_dic[item])
	overal_test_length += max_lenght
	print  "function id: ", func_id_1-1, "\ttest length:", max_lenght

stop_time = time.time()

final_unused_patterns = copy.deepcopy(package.final_un_used_pattern(number_of_lines, final_set_of_patterns))

for item in sorted(final_set_of_patterns):
	test_patterns_file.write(str(function_dict[item][0])+""+str(function_dict[item][1])+"\n")

# reports!
package.report_usefull_patterns_per_round(used_dic, len_of_list)
print "overal test length:", overal_test_length
package.print_results(final_set_of_patterns, final_unused_patterns, verbose)
package.print_fault_coverage(number_of_lines, number_of_ones_in_experiments, number_of_zeros_in_experiments)

print "------------------------------------------"*3
print "program took ", str(stop_time-start_time), "seconds"

# closing all files
table_file.close()
scanning_table_file.close()
test_patterns_file.close()
saf_test_patterns_file.close()
