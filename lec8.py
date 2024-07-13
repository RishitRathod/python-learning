import numpy as np
# #one dimentional array
# n1 = np.array([10,20,30])
# print(n1)

# #two dimensional array
# n2 = np.array([[10,20,30],[40,50,60]])
# print(n2)
# print(type(n2))

# #initializing Numpy array with zero
# n3 = np.zeros((1,2))
# print(n3)
# n4 = np.zeros((5,5))
# print(n4)

# #initializing Numpy array with same number(variable)
# n5 = np.full((2,2),10)
# print(n5)

# #initializing Numpy array with a range
# n6=np.arange(10,20)
# print(n6)
# n7=np.arange(10,50,5)
# print(n7)

# #initializing Numpy array with random numbers
# n8=np.random.randint(1,100,5)
# print(n8)

# #checking the shape of numpy arrays
# n9=np.array([[1,2,3],[4,5,6]])
# print(n9)
# print(n9.shape)
# n9.shape=(3,2)
# print(n9)

# joining Numpy Arrays
# vstack(), hstack(),column_stack()
# n10 = np.array([10,20,30])
# n11 = np.array([40,50,60])
# print(np.vstack((n10,n11)))
# print(np.hstack((n10,n11)))
# print(np.column_stack((n10,n11)))

# #numpy intersection and difference
# n12=np.array([10,20,30,40,50])
# n13=np.array([50,40,70,80])
# print(np.intersect1d(n12,n13))
# print(np.setdiff1d(n12,n13))

# #addition of numpy array
# n14=np.array([10,20])
# n15=np.array([30,40])
# print(np.sum([n14,n15]))
# print(np.sum([n14,n15],axis=0))
# print(np.sum([n14,n15],axis=1))

#numpy array basic mathematics
n16=np.array([10,20,30])
print(n16/2)
print(n16+1)
print(n16-1)
print(n16*2)
print(n16**2)
