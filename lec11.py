import numpy as np
# #task 1
# #broadcasting
# #create 1D array
# a1=np.array([1,2,3])
# #create 2D array
# a2=np.array([[1],[2],[3]])
# print(a1)
# print(a2)
# print(a1+a2)

# #task 2
# #broadcasting with scaling
# a3=np.array([1,2,3])
# num=5
# sum=a3+num
# print(sum)


# #task3
# # Numpy matrix operation in Numpy (real Matrai Multiplication)
# mt1 = np.array([[1,2],[3,4]])
# mt2 = np.array([[5,6],[7,8]])
# result = np.dot(mt1,mt2)
# print(result,"\n")


# #task4
# mt1 = np.array([[1,2],[3,4]])
# mt2 = np.array([[5,6],[7,8]])
# # Transpose
# result = np.transpose(mt1)
# print(result,"\n")


# #task5
# # Inverse
# mat1 = np.array([[1,2,3],[2,3,1],[4,3,1]])
# result = np.invert(mat1)
# print(result)


# #task6 find determinant
# mat1 = np.array([[1,2,3],[2,3,1],[4,3,1]])
# result=np.linalg.det(mat1)
# print(result)


# #task7 flatten matrix in numpy
# ma1=np.array([[1,2,3],[4,6,7],[8,9,10]])
# ma2=np.array([[1],[2],[3]])
# result=ma1.flatten()
# print(result)

# #task8 numpy array iterating
# arr=np.array([1,2,3])
# for x in arr:
#     print(x)

#task9
#iterating 2D array
arr=np.array([[1,2,3],[4,5,6]]) 
for x in arr:
    for y in x:
      print(y)
a=np.array([[1,3,3]]) 
print(a)
a=np.array([1,3,3]) 
print(a)
