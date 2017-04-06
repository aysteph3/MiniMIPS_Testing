# Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran

import Logger
import sys
import copy
import time
import package



package.generate_folders(package.generated_files_folder)
sys.stdout = Logger.Logger(package.generated_files_folder)

if "-sp" in sys.argv[1:]:
	saf_output_patterns_file_name= package.generated_files_folder + "/" +"SAF"+ sys.argv[sys.argv.index('-sp') + 1]
else:
	saf_output_patterns_file_name= package.generated_files_folder + "/" + "SAFpatterns.txt"

input_file_name, verbose, debug, output_table_file_name, output_patterns_file_name, scanning_table_file_name, redundant_function_reduction= package.parse_program_arg(sys.argv, package.generated_files_folder)

data_width = package.data_width
print "data_width:", data_width


start_time = time.time()

function_dict = copy.deepcopy(package.parse_input_pattern_file(input_file_name))
len_of_list = len(function_dict[function_dict.keys()[0]])
number_of_lines = len(function_dict.keys())

try:
	table_file = open(output_table_file_name, 'w')
	scanning_table_file = open(scanning_table_file_name, 'w')
	saf_test_patterns_file = open(saf_output_patterns_file_name, 'w')
	test_patterns_file = open(output_patterns_file_name, 'w')
except IOError:
    print "Could not open input pattern file, test pattern file, conformity or scanning table file!"
    sys.exit()

deletion_dic = {}
used_dic = {}
number_of_ones_in_experiments = 0
number_of_zeros_in_experiments = 0
final_set_of_patterns = []

if package.test_subset:
	function_list = []
	for item in package.test_only_list:
		function_list.append(item+1)
else:
	function_list = range(2, len_of_list)

package.make_table_header(table_file, function_list)
package.make_table_header(scanning_table_file, function_list)

for func_id_1 in function_list:
	string =  '%10s' %("f_"+str(func_id_1-1)+"|") 			# -1 to march the number of functions for readability
	scanning_string =  '%10s' %("f_"+str(func_id_1-1)+"|") 	# -1 to march the number of functions for readability
 	if "F"+str(func_id_1-1) in  package.pre_determinde_patterns.keys():
	 	list_of_used_patterns = package.pre_determinde_patterns["F"+str(func_id_1-1)]
		list_of_necessary_patterns = []
		scanning_test_f1 = "0"*data_width
		for func_id_2 in function_list:
			scanning_test_f1_f2 = "0"*data_width
			if func_id_1 != func_id_2:

				list_of_pattens_to_delete = []
				if verbose:
					print "---------------------------------------------------------------------------------------"
					print "---------------------------------------------------------------------------------------"
					print "function_1: ", func_id_1-1, "function_2:", func_id_2-1
					print "line\top1\t\top2\t\tfunc_1 \t\t func_2\t\txor(1,2)\tand(1,xor)\tor(prev_or,and)"
					print "---------------------------------------------------------------------------------------"
					print "starting with list: ", list_of_necessary_patterns

				or_op = "0"*data_width
				for i in list_of_necessary_patterns:
					xor_op = format(int(function_dict[i][func_id_1], 2) ^ int(function_dict[i][func_id_2], 2), 'b').zfill(data_width)
					and_op = format(int(function_dict[i][func_id_2], 2) & int(xor_op, 2), 'b').zfill(data_width)
					or_op = format(int(or_op, 2) | int(and_op, 2), 'b').zfill(data_width)
					if verbose:
						print str(i)+"\t", function_dict[i][0],"\t", function_dict[i][1],"\t", function_dict[i][func_id_1], "\t", function_dict[i][func_id_2], "\t", xor_op, "\t"+str(and_op), "\t"+str(or_op)
				# print list_of_used_patterns
				for i in list_of_used_patterns:
					if i not in list_of_necessary_patterns:
						xor_op = format(int(function_dict[i][func_id_1], 2) ^ int(function_dict[i][func_id_2], 2), 'b').zfill(data_width)
						and_op = format(int(function_dict[i][func_id_2], 2) & int(xor_op, 2), 'b').zfill(data_width)
						prev_or = or_op
						or_op = format(int(or_op, 2) | int(and_op, 2), 'b').zfill(data_width)
						if prev_or == or_op or or_op == "0"*data_width:
							if i not in list_of_necessary_patterns:
								list_of_pattens_to_delete.append(i)
								# print "adding pattern:", i, "to unused list"
						else:
							if or_op != "0"*data_width:
								if i not in list_of_necessary_patterns:
									list_of_necessary_patterns.append(i)
									if verbose:
										print str(i)+"\t", function_dict[i][0],"\t", function_dict[i][1],"\t", function_dict[i][func_id_1], "\t", function_dict[i][func_id_2], "\t", xor_op, "\t"+str(and_op), "\t"+str(or_op) , "\t\tadding pattern ", i, "to final pattern list!"
							if or_op == "1"*data_width:
								if verbose:
									print  "INFO::  reached all ones!"
								break
				if or_op != "1"*data_width:
					if verbose:
						print  "INFO::  Didn't find a solution!"

				string += "\t"+str(or_op)

				number_of_ones_in_experiments  += or_op.count("1")
				if redundant_function_reduction:
					if  (str(func_id_1-1)+"_"+str(func_id_2-1) in package.related_functions.keys()):
						number_of_zeros_in_experiments  += or_op.count("0") - package.related_functions[str(func_id_1-1)+"_"+str(func_id_2-1)].count("0")
					elif (str(func_id_1-1)+"_*" in package.related_functions.keys()):
						number_of_zeros_in_experiments  += or_op.count("0") - package.related_functions[str(func_id_1-1)+"_*"].count("0")
					elif ("*_"+str(func_id_2-1) in package.related_functions.keys()):
						number_of_zeros_in_experiments  += or_op.count("0") - package.related_functions["*_"+str(func_id_2-1)].count("0")
					else:
						number_of_zeros_in_experiments  += or_op.count("0")
				else:
					number_of_zeros_in_experiments  += or_op.count("0")
				if verbose:
					print "------------------------------"

				for scan_pattern in list_of_necessary_patterns:
					scanning_test_f1_f2 = format(int(scanning_test_f1_f2, 2) | int(function_dict[scan_pattern][func_id_1], 2), 'b').zfill(data_width)


				if verbose:
					print "final list of patterns:", list_of_necessary_patterns
				for final_pattern in list_of_necessary_patterns:
					if final_pattern not in final_set_of_patterns:
						final_set_of_patterns.append(final_pattern)

				# print "final list of unused patterns:", list_of_pattens_to_delete
				deletion_dic['{0:03}'.format(func_id_1)+"_"+'{0:03}'.format(func_id_2)] = copy.deepcopy(list_of_pattens_to_delete)
				used_dic['{0:03}'.format(func_id_1)+"_"+'{0:03}'.format(func_id_2)] = copy.deepcopy(list_of_necessary_patterns)

			else:
				string += "\t"+"x"*data_width

			scanning_test_f1 =  format(int(scanning_test_f1, 2) | int(scanning_test_f1_f2, 2), 'b').zfill(data_width)
			scanning_string += "\t"+str(scanning_test_f1_f2)

		#-------------------------------------------------------------------------------
		#	This part fixes the scanning test results for the current function pair
		#-------------------------------------------------------------------------------
		scanning_test_f1, list_of_necessary_patterns = package.run_scanning_optimization(scanning_test_f1, function_dict, func_id_1, debug, verbose, list_of_necessary_patterns)
		scanning_string += "\t"+str(scanning_test_f1)
		scanning_table_file.write(scanning_string+"\n")
		table_file.write(string+"\n")

		# Print patterns and functions.. This will be used to prepare test patterns for SAF testing in turbo tester
		# This should only be used for VLIW experiment. Modification will be needed for other processors
		if verbose:
			print "-----------------------------------------------------"
			print "function_1: ",func_id_1

		opcode = "{0:04b}".format((func_id_1-2))
		for j in list_of_necessary_patterns:
			saf_test_patterns_file.write(function_dict[j][0]+function_dict[j][1]+opcode+"\n")

# final set of patterns
for k in final_set_of_patterns:
	test_patterns_file.write(function_dict[k][0]+function_dict[k][1]+"\n")

overal_test_length =0
for func_id_1 in range(2, len_of_list):
	max_lenght = 0
	for item in used_dic.keys():
		if int(item.split("_")[0]) == func_id_1:
			if len(used_dic[item])>max_lenght:
				max_lenght = len(used_dic[item])
	overal_test_length += max_lenght
	print  "function id: ", func_id_1-1, "\ttest length:", max_lenght

table_file.close()
scanning_table_file.close()
test_patterns_file.close()
saf_test_patterns_file.close()
stop_time = time.time()

final_unused_patterns = copy.deepcopy(package.final_un_used_pattern(number_of_lines, final_set_of_patterns))

package.report_usefull_patterns_per_round(used_dic, len_of_list)
print "overal test length:", overal_test_length
package.print_results(final_set_of_patterns, final_unused_patterns, verbose)
package.print_fault_coverage(number_of_lines, number_of_ones_in_experiments, number_of_zeros_in_experiments)

print "------------------------------------------"*3
print "program took ", str(stop_time-start_time), "seconds"
