import copy
def del_first_column(filen):
	d = {}
  	line_counter = 0
  	#out = open('o2.txt', 'w')
	with open(filename) as f:
		for line in f:
			if line != "":
				line_counter +=1
				list_of_data = line.split(" ")
				d[line_counter] = list_of_data[1:]
	return d

         #d[int(key)] = val
         #print d[1:3]
         #out.write(str(d[1:3]))
  #print len(d)
  #print d[1:3]
  #out.close()


out = open('o2.txt', 'w')
filename = "o.txt"
#print del_first_column(filename)
data = copy.deepcopy(del_first_column(filename))
len_of_data = len(data[data.keys()[0]])

for key in data:
	print key
	string = ""
	for j in range (len_of_data):
		print data[key][j]
		string += data[key][j]+" "
		out.write(string.strip(" "))
		#out.write('%s ' % data[key][j].strip(" "))
	#out.write('\n')
out.close()