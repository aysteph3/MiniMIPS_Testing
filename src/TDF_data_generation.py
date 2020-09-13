inputFile = "../sim_generated_file/test.txt"
try:
    functional_result = open(inputFile, 'r')
    lenght_file = open(inputFile, 'r')
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit")

lines = functional_result.readlines()
lenght_of_line = len(lenght_file.readline().split())
for number in range(2,lenght_of_line):
    f_res = '00000000000000000000000000000000'
    prev_res = '00000000000000000000000000000000'
    for line in lines:
        data = line.split()
        f_res = format((int(f_res,2) | int(data[number],2)), 'b').zfill(32)
        print f_res
        if f_res == '11111111111111111111111111111111':
            break
        #if prev_res == format(int(data[number],2),'b').zfill(32):
        if prev_res != '00000000000000000000000000000000':
            if f_res == prev_res:
                #print prev_res
                #print f_res
                prev_res = f_res
                break
    print('\n')

functional_result.close()
lenght_file.close()
