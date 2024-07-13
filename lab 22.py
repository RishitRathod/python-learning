#lab 22


# Wriet Mode
# Task 1: Open a file for writing and insert some 
f = open('ICT.txt','w')
f.write('PWP\n')
f.write('COA \n')
f.write('ICE\n')
f.write('DMGT\n')
f.write('SS\n')
f.close()


# # Task 2: Append COde 
# f = open('ICT.txt','a')
# f.write('DS\n')
# f.close()

# # Task 3: Open the file created for reading and read line(s) using readline()
# f=open('ICT.txt','r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()


# # Task 4: Exeption Handling in Files
# try:
#     f=open('ICT.txt','r')
#     g = f.readline() # REad next line into a string
#     print(g) # read all (next) lines into a list of strings
# finally:
#     f.close()

# # Task 5: PRocessing (with statement is equivalent to try-finally start )
# with open('ICT.txt','r') as f:
#     for line in f:
#         line = line.strip() # strip the leading/trailing whitespaces and 
#     # file closed automatically upor exit of with- statement

# # Task 6: Deleting Files
# import os as d
# d.remove("ICT.txt")  


# # write a code create one txt file and copy all content to other file
# # created one file
# f = open('naam.txt','w')
# f.write(' Kirtan ')
# f.write('Makwana ')
# # read that file
# f = open('naam.txt','r')
# k = f.readline()

# f1 = open('namcopy.txt','w')
# # copied data in other file 
# f1.write(k)
# f1.close()
# f.close()


################################### POST LAB #################################

# # Creating a binary file and writing data to it
# with open('binary_data.bin', 'wb') as file:
#     data_to_write = b'\x01'  
#     file.write(data_to_write)

# # Reading data from the binary file
# with open('binary_data.bin', 'rb') as file:
#     read_data = file.read()

# # Displaying the read data
# print("Data read from the binary file:", read_data)

# # Converting the binary data to a string (if applicable)
# read_string = read_data.decode('utf-8')  # Assuming the data is encoded as UTF-8
# print("String representation of the data:", read_string)