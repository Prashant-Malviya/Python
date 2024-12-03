'''



'''

# in open method by default there is read(r) 

# f = open('file.txt')

# data = f.read()
# updateData = f.write('updated this file')
# # print(data)
# f.close()

# st = "hey prashant how are you and ur family"

# f = open('myfile.txt','w')

# f.write(st)

# f.close()



f = open('myfile.txt')

# lines = f.readlines()
# print(lines,type(lines))

# line1 = f.readline()

# print(line1,type(line1))

# line2 = f.readline()

# print(line2,type(line2))

# f.close()

# line = f.readline()

# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()


'''
modes of opening a file

r = open for reading
w = writing
a = open for appending
+ = open for updating
rb = will open for read in binary moda
rt = will open for read i txt mode

'''

st = 'jai shre krishna'

f = open('myfile.txt','a')

f.write(st)

f.close()