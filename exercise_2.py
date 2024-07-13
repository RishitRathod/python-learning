# #task 1
# for i in range(0,10):
#     for j in range(0,10):
#         print("*",end=" ")
#     print()

# #task 2
# s=0
# f=0
# for i in range(0,101):
#     if(i%2==0):
#         s=s+i
#     else:
#         f=f+i
# print("sum of even numbers",s)
# print("sum of odd numbers",f)        

# #task 3
# for i in range(10,31):
#     print(i*10)

# #task 4
# n=105
# while n>=7:
#     print(n)
#     n-=7

#task5
# n=int(input("enter a number"))
# i=n
# s=0
# while i>1:
#     if(n%i==0):
#         s=s+1
#     i=i-1
# if(s<=2):
#     print("prime number")
# else:
#     print("not")

# #task 6
# n=input("enter a number")
# s=n[::-1]
# print(s)

# task 7
#n=input("enter a number")



# #task 8
n=input("enter a number")
s=n[::-1]
if(n==s):
    print("palindrome")
else:
    print("not")