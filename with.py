# f = open('file.txt')

# print(f.read())

# f.close()

# ths same can be written with with statment like this 


with open('myfile.txt') as f:
    print(f.read())

    #now you need not to close the file explictely
