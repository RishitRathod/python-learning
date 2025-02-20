from scipy import fftpack
from matplotlib import pyplot as plt
import numpy as np 
import seaborn as sns
# #task 1
# sns.set_style("darkgrid")
# #Frequency in terms of Hertz
# fre  = 60
# #Sample rate
# fre_samp = 60
# t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
# a = np.sin(fre  * 2 * np.pi * t)
# plt.plot(t, a)
# plt.xlabel('Time (s)')
# plt.ylabel('Signal amplitude')
# plt.show()
# A = fftpack.fft(a)
# frequency = fftpack.fftfreq(len(a)) * fre_samp
# plt.stem(frequency, np.abs(A),use_line_collection=True)
# plt.xlabel('Frequency in Hz')
# plt.ylabel('Frequency Spectrum Magnitude')
# plt.show()

# #task 2 SciPy integrate
# from numpy import exp  
# f= lambda x:exp(-x**2)  
# import scipy 
# i = scipy.integrate.quad(f, 0, 1)  
# print(i)  


# #task 3 Multiple Integrals
# import scipy.integrate  
# from numpy import exp  
# from math import sqrt  
# f = lambda x, y : 2*x*y  
# g = lambda x : 0 
# h = lambda y : 4*y**2 
# i = scipy.integrate.dblquad(f, 0, 0.5, g, h)  
# print(i)

# #task 4 SciPy Interpolation
# import numpy as np  
# from scipy import interpolate  
# import matplotlib.pyplot as plt  
x = np.linspace(0, 5, 10)  
y = np.cos(x**2/3+4) 
# plt.scatter(x,y,c='r')  
# plt.show()  

# #task 5
# from scipy.interpolate import interp1d  
# import matplotlib.pyplot as plt  
# fun1 = interp1d(x, y,kind = 'linear')  
# fun2 = interp1d(x, y, kind = 'cubic')  
# #we define a new set of input
# xnew = np.linspace(0, 4,30)  
# plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
# plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')  
# plt.show()

# #task 6
# # Now what happens when we change the input values
# from scipy.interpolate import interp1d  
# import matplotlib.pyplot as plt  
# fun1 = interp1d(x, y,kind = 'linear')  
# fun2 = interp1d(x, y, kind = 'cubic')  
# xnew = np.linspace(3, 5,30)  
# plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
# plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')  
# plt.show()  


# # #task 7
# import numpy as np  
# from scipy import linalg  
# # We are trying to solve a linear algebra system which can be given as   
# #         x + 2y - 3z = -3 
# #         2x - 5y + 4z = 13  
# #         5x + 4y - z = 5  
# #We will find values of x,y and z for which all these equations are zero
# # Also finally we will check if the values are right by substituting them in the equations
# # Creating input array  
# a = np.array([[1, 2, -3], [2, -5, 4], [5, 4, -1]])  
# # Solution Array  
# b = np.array([[-3], [13], [5]])  
# # Solve the linear algebra  
# x = linalg.solve(a, b) 
# # Print results  
# print(x)  
# # Checking Results  
# print("\n Checking results,must be zeros")  
# print(a.dot(x) - b) 


# # #task 8 Finding a determinant of a square matrix
# #importing the scipy and numpy packages
# from scipy import linalg
# import numpy as np 
# #Declaring the numpy array
# A = np.array([[1,2,9],[3,4,8],[7,8,4]])
# #Passing the values to the det function
# x = linalg.det(A)
# #printing the result
# print('Determinant of \n{} \n is {}'.format(A,x))


# #task 9Eigenvalues and Eigenvectors
# #importing the scipy and numpy packages
# from scipy import linalg
# import numpy as np 
# #Declaring the numpy array
# A = np.array([[2,1,-2],[1,0,0],[0,1,0]])  
# #Passing the values to the eig function
# values, vectors = linalg.eig(A) 
# #printing the result for eigenvalues
# print(values) 
# #printing the result for eigenvectors
# print(vectors)



# #task 10 SciPy Ndimage
# import scipy.misc
# import matplotlib.pyplot as plt
# face = scipy.misc.face()#returns an image of raccoon
# #display image using matplotlib
# plt.imshow(face)
# plt.show()

# # task 12 Crop image
# import scipy.misc
# import matplotlib.pyplot as plt
# face = scipy.misc.face()#returns an image of raccoon
# lx,ly,channels= face.shape
# # Cropping
# crop_face = face[int(lx/4):int(-lx/4), int(ly/4):int(-ly/4)]
# plt.imshow(crop_face)
# plt.show()

# #task 13 Rotate Image
# from scipy import misc,ndimage
# import matplotlib.pyplot as plt
# face = misc.face()
# rotate_face = ndimage.rotate(face, 180)
# plt.imshow(rotate_face)
# plt.show()

# #task 14 Blurring or Smoothing  Images
# import scipy
# from scipy import ndimage,misc
# import matplotlib.pyplot as plt
# face = scipy.misc.face(gray=True)
# blurred_face = ndimage.gaussian_filter(face, sigma=3)
# very_blurred = ndimage.gaussian_filter(face, sigma=5)
# plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.imshow(face, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplot(132)
# plt.imshow(very_blurred, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplot(133)
# plt.imshow(blurred_face, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,left=0.01, right=0.99) 
# plt.show()

# #task 15 Sharpening images
# import scipy
# from scipy import ndimage
# import matplotlib.pyplot as plt
# f = scipy.misc.face(gray=True).astype(float)
# blurred_f = ndimage.gaussian_filter(f, 3)
# filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
# alpha = 30
# sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.imshow(f, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplot(132)
# plt.imshow(blurred_f, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplot(133)
# plt.imshow(sharpened, cmap=plt.cm.gray)
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# #task 16 Edge detection
# import numpy as np
# from scipy import ndimage
# import matplotlib.pyplot as plt
# im = np.zeros((256, 256))
# im[64:-64, 64:-64] = 1 
# im = ndimage.rotate(im, 15, mode='constant')
# im = ndimage.gaussian_filter(im, 8) 
# sx = ndimage.sobel(im, axis=0, mode='constant')
# sy = ndimage.sobel(im, axis=1, mode='constant')
# sob = np.hypot(sx, sy)
# plt.figure(figsize=(9,5))
# plt.subplot(141)
# plt.imshow(im)
# plt.axis('off')
# plt.title('square', fontsize=20)
# plt.subplot(142)
# plt.imshow(sob)
# plt.axis('off')
# plt.title('Sobel filter', fontsize=20)
# plt.show()


# # Post Lab 

# # Task - 1 :- Calculating Inverses and Determinants With scipy.linalg
# import numpy as np
# from scipy.linalg import inv, det
# rows = int(input("Enter The Number Of Rows :- "))
# columns = int(input("Enter The Number Of Columns :- "))
# A = np.empty((rows, columns))
# if(rows == columns ) :    
#     for i in range(0,rows) :
#         for j in range(0,columns) :
#             element = int(input(f"Enter The Integer On {i + 1 } th Row and {j + 1 } th Columns :- "))
#             A[i][j] = element
#     A_inv = inv(A)
#     det_A = det(A)
#     print("Original Matrix A:")
#     print(A)
#     print("Inverse of A:")
#     print(A_inv)
#     print("Determinant of A:", det_A)  
# else :
#     print("Enter Valid Dimmenssions Of A Matrix.")


# # Task - 2 :- Interpolating Polynomials with Linear Systems (Y = P(X) = a0 + a1X + a2X^2)
# import numpy as np
# from scipy.interpolate import lagrange

# x = np.array([0, 1, 2, 3])
# y = np.array([1, 3, 5, 7])
# p = lagrange(x, y)
# x_new = float(input("Enter The Value Of X to Get Value Of Y For The Function :- Y = P(X) = a0 + a1X + a2X^2 :- "))
# y_new = p(x_new)
# print(y_new)