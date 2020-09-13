#!/usr/bin/env python
# Copyright (C) 2020 Stephen Oyeniran

def remove_duplicate():
	inputF = "TDFdata.txt"
	try:
		inputData = open(inputF, 'r')
	except IOError:
		print("File not found or path is incorrect")

	lines_seen = set() # holds lines already seen
	with open("tdf_data_noduplicate.txt", "w") as output_file:
		for each_line in inputData:
			if each_line not in lines_seen: # check if line is not duplicate
				output_file.write(each_line)
	        	lines_seen.add(each_line)
	inputData.close()
