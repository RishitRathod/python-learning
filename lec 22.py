
f = open('PYTHON.txt','w')
f.write('PWP\n')
f.write('COA\n')
f.write('DMGT\n')
f.write('ICE\n')
f.write('SS\n')
f.close()

# f = open("PYTHON.txt",'a')##append mode
# f.write("DS\n")

# f = open("PYTHON.txt",'r')##read mode
# print(f.readline())
# print(f.readlines())
# print(f.readline())

# try:
#     f = open("PYTHON.txt",'r')##exception handling
#     g = f.readline()
#     print(g)
# finally:
#     f.close()
    
# with open("PYTHON.txt",'r') as f:
#     for line in f:
#         line = line.strip()#strip the leading and trailing whitespaces

# import os as d
# d.remove("PYTHON.txt")#delete file

# print('Hello, my name is', self.name)

# f = open("DSA.txt",'w')##write mode
# print(f.writable())
# f = open("DSA.txt",'r')##read mode
# print(f.writable())

f = open("DSA.txt",'w')##write mode
print(f.readable())
f = open("DSA.txt",'r')##read mode
print(f.readable())