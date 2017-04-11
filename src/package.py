# Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran

import sys, os
# in this dictionary we describe untestable points between related functions!

# use the function number in the table file!
# "10000000" means that only the most significant bit is provable to be testable
# "01111111" the most significant bit is not testable
related_functions = {
						"2_1"  		: "00000000000000000000000000000000",
						"3_1"  		: "11111111111111111111111111111110",
						"4_1"  		: "11111111111111111111111111111110",
						"6_1"  		: "11111111111111111111111111111110",
						"7_1"  		: "11111111111111111111111111111110",
						"12_1"  	: "11111111111111111111111111111110",
						"27_1"  	: "11111111111111111111111111111110",
						"1_2"  		: "00000000000000000000000000000000",
						"3_2"  		: "11111111111111111111111111111110",
						"4_2"  		: "11111111111111111111111111111110",
						"6_2"  		: "11111111111111111111111111111110",
						"7_2"  		: "11111111111111111111111111111110",
						"12_2"  	: "11111111111111111111111111111110",
						"27_2"  	: "11111111111111111111111111111110",
						"1_3"  		: "11111111111111111111111111111110",
						"2_3"  		: "11111111111111111111111111111110",
						"4_3"  		: "00000000000000000000000000000000",
						"6_3"  		: "11111111111111111111111111111110",
						"7_3"  		: "11111111111111111111111111111110",
						"12_3"  	: "11111111111111111111111111111110",
						"27_3"  	: "11111111111111111111111111111110",
						"1_4"  		: "11111111111111111111111111111110",
						"2_4"  		: "11111111111111111111111111111110",
						"3_4"  		: "00000000000000000000000000000000",
						"6_4"  		: "11111111111111111111111111111110",
						"7_4"  		: "11111111111111111111111111111110",
						"12_4"  	: "11111111111111111111111111111110",
						"27_4"  	: "11111111111111111111111111111110",
						"6_5"  		: "00000000000000000000000000000000",
						"12_5"  	: "11111111111111111111111111111110",
						"21_5"  	: "01111111111111111111111111111111",
						"25_5"  	: "00000000000000000000000000000000",
						"26_5"  	: "00000000000000000000000000000000",
						"27_5"  	: "11111111111111111111111111111110",
						"12_6"  	: "11111111111111111111111111111110",
						"27_6"  	: "11111111111111111111111111111110",
						"1_7"  		: "11111111111111111111111111111110",
						"2_7"  		: "11111111111111111111111111111110",
						"3_7"  		: "11111111111111111111111111111110",
						"4_7"  		: "11111111111111111111111111111110",
						"6_7"  		: "00000000000000000000000000000000",
						"12_7"  	: "11111111111111111111111111111110",
						"27_7"  	: "11111111111111111111111111111110",
						"27_8"  	: "11111111111111111111111111111110",
						"1_9"  		: "00000000000000000000000000000001",
						"2_9"  		: "00000000000000000000000000000001",
						"3_9"  		: "00000000000000000000000000000001",
						"4_9"  		: "00000000000000000000000000000001",
						"5_9"  		: "00000000000000000000000000000001",
						"6_9"  		: "00000000000000000000000000000001",
						"7_9"  		: "00000000000000000000000000000001",
						"8_9"  		: "00000000000000000000000000000001",
						"10_9"  	: "00000000000000000000000000000001",
						"11_9"  	: "00000000000000000000000000000001",
						"12_9"  	: "00000000000000000000000000000000",
						"13_9"  	: "00000000000000000000000000000001",
						"14_9"  	: "00000000000000000000000000000001",
						"15_9"  	: "00000000000000000000000000000001",
						"16_9"  	: "00000000000000000000000000000001",
						"17_9"  	: "00000000000000000000000000000001",
						"18_9"  	: "00000000000000000000000000000001",
						"19_9"  	: "00000000000000000000000000000001",
						"20_9"  	: "00000000000000000000000000000001",
						"21_9"  	: "00000000000000000000000000000001",
						"22_9"  	: "00000000000000000000000000000001",
						"23_9"  	: "00000000000000000000000000000001",
						"24_9"  	: "00000000000000000000000000000001",
						"25_9"  	: "00000000000000000000000000000001",
						"26_9"  	: "00000000000000000000000000000001",
						"27_9"  	: "00000000000000000000000000000000",
						"28_9"  	: "00000000000000000000000000000001",
						"1_10"  	: "00000000000000000000000000000001",
						"2_10"  	: "00000000000000000000000000000001",
						"3_10"  	: "00000000000000000000000000000001",
						"4_10"  	: "00000000000000000000000000000001",
						"5_10"  	: "00000000000000000000000000000001",
						"6_10"  	: "00000000000000000000000000000001",
						"7_10"  	: "00000000000000000000000000000001",
						"8_10"  	: "00000000000000000000000000000001",
						"9_10"  	: "00000000000000000000000000000001",
						"11_10"  	: "00000000000000000000000000000001",
						"12_10"  	: "00000000000000000000000000000000",
						"13_10"  	: "00000000000000000000000000000001",
						"14_10"  	: "00000000000000000000000000000001",
						"15_10"  	: "00000000000000000000000000000001",
						"16_10"  	: "00000000000000000000000000000001",
						"17_10"  	: "00000000000000000000000000000001",
						"18_10"  	: "00000000000000000000000000000001",
						"19_10"  	: "00000000000000000000000000000001",
						"20_10"  	: "00000000000000000000000000000001",
						"21_10"  	: "00000000000000000000000000000001",
						"22_10"  	: "00000000000000000000000000000001",
						"23_10"  	: "00000000000000000000000000000001",
						"24_10"  	: "00000000000000000000000000000001",
						"25_10"  	: "00000000000000000000000000000001",
						"26_10"  	: "00000000000000000000000000000001",
						"27_10"  	: "00000000000000000000000000000000",
						"28_10"  	: "00000000000000000000000000000001",
						"1_11"  	: "00000000000000000000000000000001",
						"2_11"  	: "00000000000000000000000000000001",
						"3_11"  	: "00000000000000000000000000000001",
						"4_11"  	: "00000000000000000000000000000001",
						"5_11"  	: "00000000000000000000000000000001",
						"6_11"  	: "00000000000000000000000000000001",
						"7_11"  	: "00000000000000000000000000000001",
						"8_11"  	: "00000000000000000000000000000000",
						"9_11"  	: "00000000000000000000000000000001",
						"10_11"  	: "00000000000000000000000000000001",
						"12_11"  	: "00000000000000000000000000000001",
						"13_11"  	: "00000000000000000000000000000001",
						"14_11"  	: "00000000000000000000000000000001",
						"15_11"  	: "00000000000000000000000000000000",
						"16_11"  	: "00000000000000000000000000000000",
						"17_11"  	: "00000000000000000000000000000000",
						"18_11"  	: "00000000000000000000000000000001",
						"19_11"  	: "00000000000000000000000000000001",
						"20_11"  	: "00000000000000000000000000000001",
						"21_11"  	: "00000000000000000000000000000001",
						"22_11"  	: "00000000000000000000000000000001",
						"23_11"  	: "00000000000000000000000000000001",
						"24_11"  	: "00000000000000000000000000000001",
						"25_11"  	: "00000000000000000000000000000001",
						"26_11"  	: "00000000000000000000000000000001",
						"27_11"  	: "00000000000000000000000000000000",
						"28_11"  	: "00000000000000000000000000000001",
						"1_12"  	: "00000000000000000000000000000001",
						"2_12"  	: "00000000000000000000000000000001",
						"3_12"  	: "00000000000000000000000000000001",
						"4_12"  	: "00000000000000000000000000000001",
						"5_12"  	: "00000000000000000000000000000001",
						"6_12"  	: "00000000000000000000000000000001",
						"7_12"  	: "00000000000000000000000000000001",
						"8_12"  	: "00000000000000000000000000000001",
						"9_12"  	: "00000000000000000000000000000001",
						"10_12"  	: "00000000000000000000000000000001",
						"11_12"  	: "00000000000000000000000000000001",
						"13_12"  	: "00000000000000000000000000000001",
						"14_12"  	: "00000000000000000000000000000001",
						"15_12"  	: "00000000000000000000000000000001",
						"16_12"  	: "00000000000000000000000000000001",
						"17_12"  	: "00000000000000000000000000000001",
						"18_12"  	: "00000000000000000000000000000001",
						"19_12"  	: "00000000000000000000000000000001",
						"20_12"  	: "00000000000000000000000000000001",
						"21_12"  	: "00000000000000000000000000000001",
						"22_12"  	: "00000000000000000000000000000001",
						"23_12"  	: "00000000000000000000000000000001",
						"24_12"  	: "00000000000000000000000000000001",
						"25_12"  	: "00000000000000000000000000000001",
						"26_12"  	: "00000000000000000000000000000001",
						"27_12"  	: "00000000000000000000000000000000",
						"28_12"  	: "00000000000000000000000000000001",
						"1_13"  	: "00000000000000000000000000000001",
						"2_13"  	: "00000000000000000000000000000001",
						"3_13"  	: "00000000000000000000000000000001",
						"4_13"  	: "00000000000000000000000000000001",
						"5_13"  	: "00000000000000000000000000000001",
						"6_13"  	: "00000000000000000000000000000001",
						"7_13"  	: "00000000000000000000000000000001",
						"8_13"  	: "00000000000000000000000000000001",
						"9_13"  	: "00000000000000000000000000000001",
						"10_13"  	: "00000000000000000000000000000001",
						"11_13"  	: "00000000000000000000000000000001",
						"12_13"  	: "00000000000000000000000000000000",
						"14_13"  	: "00000000000000000000000000000001",
						"15_13"  	: "00000000000000000000000000000000",
						"16_13"  	: "00000000000000000000000000000001",
						"17_13"  	: "00000000000000000000000000000001",
						"18_13"  	: "00000000000000000000000000000001",
						"19_13"  	: "00000000000000000000000000000001",
						"20_13"  	: "00000000000000000000000000000001",
						"21_13"  	: "00000000000000000000000000000001",
						"22_13"  	: "00000000000000000000000000000001",
						"23_13"  	: "00000000000000000000000000000001",
						"24_13"  	: "00000000000000000000000000000001",
						"25_13"  	: "00000000000000000000000000000001",
						"26_13"  	: "00000000000000000000000000000001",
						"27_13"  	: "00000000000000000000000000000000",
						"28_13"  	: "00000000000000000000000000000001",
						"1_14"  	: "00000000000000000000000000000001",
						"2_14"  	: "00000000000000000000000000000001",
						"3_14"  	: "00000000000000000000000000000001",
						"4_14"  	: "00000000000000000000000000000001",
						"5_14"  	: "00000000000000000000000000000001",
						"6_14"  	: "00000000000000000000000000000001",
						"7_14"  	: "00000000000000000000000000000001",
						"8_14"  	: "00000000000000000000000000000001",
						"9_14"  	: "00000000000000000000000000000001",
						"10_14"  	: "00000000000000000000000000000001",
						"11_14"  	: "00000000000000000000000000000001",
						"12_14"  	: "00000000000000000000000000000000",
						"13_14"  	: "00000000000000000000000000000001",
						"15_14"  	: "00000000000000000000000000000001",
						"16_14"  	: "00000000000000000000000000000000",
						"17_14"  	: "00000000000000000000000000000001",
						"18_14"  	: "00000000000000000000000000000001",
						"19_14"  	: "00000000000000000000000000000001",
						"20_14"  	: "00000000000000000000000000000001",
						"21_14"  	: "00000000000000000000000000000001",
						"22_14"  	: "00000000000000000000000000000001",
						"23_14"  	: "00000000000000000000000000000001",
						"24_14"  	: "00000000000000000000000000000001",
						"25_14"  	: "00000000000000000000000000000001",
						"26_14"  	: "00000000000000000000000000000001",
						"27_14"  	: "00000000000000000000000000000000",
						"28_14"  	: "00000000000000000000000000000001",
						"1_15"  	: "00000000000000000000000000000001",
						"2_15"  	: "00000000000000000000000000000001",
						"3_15"  	: "00000000000000000000000000000001",
						"4_15"  	: "00000000000000000000000000000001",
						"5_15"  	: "00000000000000000000000000000001",
						"6_15"  	: "00000000000000000000000000000001",
						"7_15"  	: "00000000000000000000000000000001",
						"8_15"  	: "00000000000000000000000000000001",
						"9_15"  	: "00000000000000000000000000000001",
						"10_15"  	: "00000000000000000000000000000001",
						"11_15"  	: "00000000000000000000000000000001",
						"12_15"  	: "00000000000000000000000000000001",
						"13_15"  	: "00000000000000000000000000000001",
						"14_15"  	: "00000000000000000000000000000001",
						"16_15"  	: "00000000000000000000000000000001",
						"17_15"  	: "00000000000000000000000000000001",
						"18_15"  	: "00000000000000000000000000000001",
						"19_15"  	: "00000000000000000000000000000001",
						"20_15"  	: "00000000000000000000000000000001",
						"21_15"  	: "00000000000000000000000000000001",
						"22_15"  	: "00000000000000000000000000000001",
						"23_15"  	: "00000000000000000000000000000001",
						"24_15"  	: "00000000000000000000000000000001",
						"25_15"  	: "00000000000000000000000000000001",
						"26_15"  	: "00000000000000000000000000000001",
						"27_15"  	: "00000000000000000000000000000000",
						"28_15"  	: "00000000000000000000000000000001",
						"1_16"  	: "00000000000000000000000000000001",
						"2_16"  	: "00000000000000000000000000000001",
						"3_16"  	: "00000000000000000000000000000001",
						"4_16"  	: "00000000000000000000000000000001",
						"5_16"  	: "00000000000000000000000000000001",
						"6_16"  	: "00000000000000000000000000000001",
						"7_16"  	: "00000000000000000000000000000001",
						"8_16"  	: "00000000000000000000000000000001",
						"9_16"  	: "00000000000000000000000000000001",
						"10_16"  	: "00000000000000000000000000000001",
						"11_16"  	: "00000000000000000000000000000001",
						"12_16"  	: "00000000000000000000000000000001",
						"13_16"  	: "00000000000000000000000000000001",
						"14_16"  	: "00000000000000000000000000000001",
						"15_16"  	: "00000000000000000000000000000001",
						"17_16"  	: "00000000000000000000000000000001",
						"18_16"  	: "00000000000000000000000000000001",
						"19_16"  	: "00000000000000000000000000000001",
						"20_16"  	: "00000000000000000000000000000001",
						"21_16"  	: "00000000000000000000000000000001",
						"22_16"  	: "00000000000000000000000000000001",
						"23_16"  	: "00000000000000000000000000000001",
						"24_16"  	: "00000000000000000000000000000001",
						"25_16"  	: "00000000000000000000000000000001",
						"26_16"  	: "00000000000000000000000000000001",
						"27_16"  	: "00000000000000000000000000000000",
						"28_16"  	: "00000000000000000000000000000001",
						"27_17"  	: "11111111111111111111111111111110",
						"12_18"  	: "11111111111111111111111111111110",
						"27_18"  	: "11111111111111111111111111111110",
						"1_19"  	: "11111111111111111111111111111110",
						"2_19"  	: "11111111111111111111111111111110",
						"3_19"  	: "11111111111111111111111111111110",
						"4_19"  	: "11111111111111111111111111111110",
						"6_19"  	: "11111111111111111111111111111110",
						"7_19"  	: "11111111111111111111111111111110",
						"12_19"  	: "11111111111111111111111111111110",
						"20_19"  	: "11111111111111111111111111111110",
						"21_19"  	: "11111111111111111111111111111110",
						"27_19"  	: "11111111111111111111111111111110",
						"6_20"  	: "01111111111111111111111111111111",
						"12_20"  	: "11111111111111111111111111111110",
						"19_20"  	: "01111111111111111111111111111111",
						"21_20"  	: "00000000000000000000000000000000",
						"27_20"  	: "11111111111111111111111111111110",
						"6_21"  	: "01111111111111111111111111111111",
						"12_21"  	: "11111111111111111111111111111110",
						"20_21"  	: "11111111111111111111111111111110",
						"27_21"  	: "11111111111111111111111111111110",
						"*_22"  	: "11111111111111110000000000000000",
						"*_23"  	: "00000000000000000000000000000000",
						"*_24"  	: "00000000000000000000000000000000",
						"6_25"  	: "00000000000000000000000000000000",
						"12_25"  	: "11111111111111111111111111111110",
						"26_25"  	: "00000000000000000000000000000000",
						"27_25"  	: "11111111111111111111111111111110",
						"6_26"  	: "00000000000000000000000000000000",
						"12_26"  	: "11111111111111111111111111111110",
						"25_26"  	: "00000000000000000000000000000000",
						"27_26"  	: "11111111111111111111111111111110",
						"*_27"  	: "00000000000000000000000000000001",
						"1_28"  	: "01111111111111111111111111111111",
						"2_28"  	: "01111111111111111111111111111111",
						"3_28"  	: "01111111111111111111111111111111",
						"4_28"  	: "01111111111111111111111111111111",
						"5_28"  	: "01111111111111111111111111111111",
						"6_28"  	: "01111111111111111111111111111111",
						"7_28"  	: "01111111111111111111111111111111",
						"8_28"  	: "01111111111111111111111111111111",
						"9_28"  	: "01111111111111111111111111111111",
						"10_28"  	: "01111111111111111111111111111111",
						"11_28"  	: "01111111111111111111111111111111",
						"12_28"  	: "01111111111111111111111111111110",
						"13_28"  	: "01111111111111111111111111111111",
						"14_28"  	: "01111111111111111111111111111111",
						"15_28"  	: "01111111111111111111111111111111",
						"16_28"  	: "01111111111111111111111111111111",
						"17_28"  	: "01111111111111111111111111111111",
						"18_28"  	: "01111111111111111111111111111111",
						"19_28"  	: "01111111111111111111111111111111",
						"20_28"  	: "01111111111111111111111111111111",
						"21_28"  	: "01111111111111111111111111111111",
						"22_28"  	: "01111111111111111111111111111111",
						#"23_28"  	: "01111111111111111111111111111111",
						#"24_28"  	: "01111111111111111111111111111111",
						"25_28"  	: "01111111111111111111111111111111",
						"26_28"  	: "01111111111111111111111111111111",
						"27_28"  	: "01111111111111111111111111111110",
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

test_subset = True
test_only_list = [1,2,3,4,5,6,7,8,9,10,17,18,19,20,21,23,24,25,26]
#test_only_list = [13,16]
#test_only_list = [11,12,14,15,22]

generated_files_folder = "../generated_files"
data_width  = 32

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


def make_table_header(table_file, function_list):
	"""
	writes the header for the table files
	table_file: table file, should be open!
	function_list: represents the number of functions in the experiment
	returns: None
	"""
	string =  '%10s' %(" ")
	for function in function_list:
		string += "\t"+'%32s' %("f_"+str(function-1))
	table_file.write(string+"\n")
	string = '%10s' %(" ")+ "\t" + "------------"*4*len(function_list)
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
	print "function pair", "\t", "\t", '%120s' % "usefull patterns","\t",'%10s' % "test length"
	print "-------------", "\t", "\t", '%120s' % "----------------","\t",'%10s' % "----------------"
	counter = 1
	for item in sorted(used_dic.keys()):
		print '%10s' %str(int(item.split("_")[0])-1)+"_"+str(int(item.split("_")[1])-1), "\t",'%120s' %used_dic[item], "\t",'%10s' %len(used_dic[item])
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
