import numpy as np
# #task 1
# #to check whether specified values are present in numpy array?
# c=03
# a=int(input("enter length of array"))
# arr=np.zeros(a)
# b=int(input("enter value you want to check"))
# for i in range(0,a,1):
#     arr[i]=int(input("enter value"))
# for i in range(0,a,1):
#     if(arr[i]==b):
#         c=c+1
# if(c>0):
#     print("present")
# else:
#     print("absent")    


# #2
# #reverse a numpy array
# a=int(input("enter length of array"))
# arr=np.zeros(a)
# for i in range(0,a,1):
#     arr[i]=int(input("enter value"))
# arr2=np.zeros(a)
# for j in range(0,a,1):
#     arr2[j]=arr[a-j-1]
# for j in range(0,a,1):
#     print(arr2[j])

# #3 matrix
# a=np.zeros((3,3))
# for i in range(0,3,1):
#     for j in range(0,3,1):
#         a[i][j]=int(input("enter value"))
# print(a)  
# b=2
# for i in range(0,3,1):
#     for j in range(0,3,1):
#         if(i==j):
#             continue
#         else:
#             a[i][j]=b
#         b=b+1
# print(a) 

# #4
# f1=np.loadtxt("ll.txt",dtype=float)
# print(f1)

# #5
# f1=np.loadtxt("lk.txt",skiprows=0,dtype=str)
# print(f1)
# f1=np.loadtxt("lm.txt",usecols=1,skiprows=1,dtype=str)
# for i in f1:
#     print(f1)
# f1=np.genfromtxt("lj.txt",dtypr=str,encoding=None,delimiter=",")
# print(f1)

# #6
# file = np.loadtxt("cool.txt",dtype=int)
# print(file)

# #7
# file = np.loadtxt("cool2.txt",usecols=1,skiprows=1,dtype=str)
# for i in file:
#     print(i)

# #8
# file = np.genfromtxt("cool3.txt",dtype=str,encoding = None, delimiter=",")
# print(file)
# file = np.genfromtxt("cool4.txt",dtype=str,encoding = None, skip_footer=1)
# print(file)                 


#8 obtaining boolean array from binary array
# file 
# len =  int(input("enter the length of array"))
# arr = np.zeros(len)
# for i in range(0,len,1):
#     arr[i]=int(input("enter the element of array"))
# for i in range(0,len,1):
#     if(arr[i]==0):
#         print(bool(arr[i]))
#     else:
#         print(bool(arr[i]))

# #9 getting the positions (indexes) where elements of 2 numpy arrays match
#a=np.array([1,2,3,4,5])
#b=np.array([1,2,3,4,5])
#output:[0,3,4]



import matplotlib
import numpy as np
# print(matplotlib.__version__)

from matplotlib import pyplot
import matplotlib.pyplot as plt

# #task 1 plot line
# plt.plot([1,2,3],[7,8,3])
# plt.show()
# x=np.arange(10)
# print(x)
# y=2*x+4
# plt.plot(x,y)
# plt.show()

# #task 2 draw two line
# x=[1,2,3]
# y=[2,10,5]
# plt.plot(x,y)
# plt.title("line")
# plt.ylabel('y axis')
# plt.xlabel('x axis')
# plt.show()


# #task 3 window size
# plt.plot([1,2,3],[4,2,3])
# plt.figure(figsize=(50,50))
# plt.show()

# #task 4 subplots
# plt.subplot(1,2,1)
# plt.plot([1,2,3],[3,2,1])
# plt.title('first part')
# plt.subplot(1,2,2)
# plt.plot([2,4,6],[1,2,3],"r")
# plt.title('second part')
# plt.show()

# Task 5 Important types of plots
# 1. Baar graphs
# 2. Histograms
# 3. Scatter plots
# 4. Sine plots


# # 1. Bar graphs
# plot = plt.figure()
# chars = ['A','B','C']
# values = [7,9,3]
# plt.bar(chars,values)
# plt.show()

# # 2. Histogram
# x = [20,40,60,90,50,20,70,20,20,10,90]
# num = 4
# plt.hist(x,num)
# plt.show()


# #3. Scatter plot
# a1 = [44,56,73,89,45,31]
# a2 = [10,20,30,50,40,30]
# fig = plt.figure()
# plt.scatter(a2,a1,color='r')
# plt.show()

# #4. Sine plots
# v=np.arange(0,2*np.pi,0.2)
# g=np.sin(v)
# plt.title("sine move")
# plt.plot(v,g)
# plt.show()


