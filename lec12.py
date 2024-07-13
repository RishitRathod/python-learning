import numpy as np
# #pre lab
# #1
# ma1=np.array([[2,3,4],[5,6,7],[8,9,10]])
# print(ma1)
# a=2
# arr=np.zeros((3,3)) 
# for x in range(0,3,1):
#     for y in range(0,3,1):
#         arr[x][y]=a 
#         a=a+1
# print(arr)
  

# #2
# cre=np.zeros(11)
# cre[5]=55
# print(cre)

# #3
# k=0
# d4=np.zeros((4,4))
# for x in range(0,4,1):
#     for y in range(0,4,1):
#           d4[x][y]=k
#           k=int(not(k))
#     k=int(not(k))
#     print("\n")      
# print(d4)             




# #post lab
# #1
# n=np.random.randint(1,6,5)
# print(n)


# #2
# #iterating on each scalar element
# arr=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# arr1=np.array([[1,2],[5,6]])
# for x in np.nditer(arr):
#      print(x)

#3
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)     
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

# #task3
# # sort function
# arr = np.array([3,2,0,1])
# print(np.sort(arr))
# arr = np.array(['banana','cherry','apple'])
# print(np.sort(arr))
# print("\n")

# # Numpy save and load arrays as binary file(npy,npz)
# # open a binary file in write mode
# # #task1
# arr = np.array([[[11,12,13,14],[15,16,17,18]],[[18,19,20,21],[22,23,24,25]]])
# file = open("arr","wb")
# # save array to the file
# np.save(file,arr)
# # close the file
# file.close()

# #task2
# # open the file in read binary mode
# file = open("arr","rb")
# # read the file to numpy array
# arr1 = np.load(file)
# print(arr1)
# # close the file
# file.close