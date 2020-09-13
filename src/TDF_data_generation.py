inputFile = "../sim_generated_file/test.txt"
try:
    functional_result = open(inputFile, 'r')
    tdf_data = open("TDFdata.txt", 'w')
    lenght_file = open(inputFile, 'r')
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit")

lines = functional_result.readlines()
lenght_of_line = len(lenght_file.readline().split())
for number in range(2,lenght_of_line):
    f_res = '00000000000000000000000000000000'
    prev_res = '11111111111111111111111111111111'
    count = 0
    for line in lines:
        data = line.split()
        f_res = format((int(f_res,2) | int(data[number],2)), 'b').zfill(32)
        #print f_res, data[0], data[1]
        tdf_data.write(data[0]+ data[1]+"\n")
        if f_res == '11111111111111111111111111111111':
            break

        if f_res == '00000000000000000000000000000000' and count == 5 :
            break
        prev_res = f_res
        count = count + 1
        if f_res == '00000000000000000000000000000001' or f_res == '11111111111111110000000000000000':
            break

    tdf_data.write('\n')

functional_result.close()
lenght_file.close()
