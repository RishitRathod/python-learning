import numpy as np

#1write a python code that takes in a sentence as input and display the no. of words
#no. of capital and small letters and no. of special character
a=str(input("enter a string"))
s=len(a)
c=0
d=0
e=1   #e=1 because we count space for count word and there is no space for last word
f=0
for x in range(0,s,1):
    if(a[x].isupper()==True):
            c=c+1
    elif(a[x].islower()==True):
            d=d+1
    elif(a[x]==" "):
            e=e+1
    else:
           f=f+1
print("Number of words:",e)
print("Number of capital letters:",c)
print("Number of small letters:",d)
print("Number of special symbol:",f)



# #1write a python code that takes in a sentence as input and display the no. of words
# #no. of capital and small letters and no. of special character
# a="@Python is a computer programming language"
# s=len(a)
# c=0
# d=0
# e=1   #e=1 because we count space for count word and there is no space for last word
# f=0
# for x in range(0,s,1):
#     if(a[x].isupper()==True):
#             c=c+1
#     elif(a[x].islower()==True):
#             d=d+1
#     elif(a[x]==" "):
#             e=e+1
#     else:
#            f=f+1
# print("Number of words:",e)
# print("Number of capital letters:",c)
# print("Number of small letters:",d)
# print("Number of special symbol:",f)




# #4 write a python program to check a sequence of numbers is an arithmetic progression or not
# a=np.array([1,8,27,64])
# b=np.array([1,3,7,2])
# s=len(a)
# s=s-1
# c=0
# d=0
# for i in range(0,s,1):
#     if(a[i]<a[i+1]):
#        c=c+1
#     if(b[i]<b[i+1]):
#        d=d+1   
# if(c==3):
#     print("for input [1,8,27,64]: TRUE")
# else: 
#     print("for input [1,8,27,64]:False")  
# if(d==3):
#     print("for input [1,3,7,2]: TRUE")
# else: 
#     print("for input [1,3,7,2]: False") 



# #5 write a python program to remove duplicates from a list of integers , preserving order.
# a=[1,3,4,10,4,1,43]
# a.reverse()
# s=len(a)
# s=s-3
# for i in range(0,s):
#     if(a.count(a[i])==2):
#         a.remove(a[i])
# a.reverse()
# print(a)




