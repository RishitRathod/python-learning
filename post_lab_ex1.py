# #task 1 display the factorial of a number
# s=1
# a=int(input("enter your number"))
# for i in range(1,(a+1)):
#     s=s*i
# print(s)


# #2 append the square of each number to a new list 
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in range(1,len(l1)):
#     l2.append(l1[i]*l1[1])
# print("square =",l2)



# #3 separate posi and neg from a list
# l1=[1,2,3,-4,5,6,7,8,-9,-10]
# l2=[]
# l3=[]
# for i in range(1,len(l1)):
#     if(l1[i]>0):
#         l2.append(l1[i])
#     else:
#         l3.append(l1[i])

# print(l2)
# print(l3)


# #4filter even and odd from list
# l1=[1,2,3,-4,5,6,7,8,-9,-10]
# l2=[]
# l3=[]
# for i in range(1,len(l1)):
#     if(l1[i]%2==0):
#         l2.append(l1[i])
#     else:
#         l3.append(l1[i])

# print(l2)
# print(l3)


#5 all even number between given range
# a=int(input("enter your number"))
# l2=[]
# for i in range(1,a):
#     if(i%2==0):
#         l2.append(i)
# print(l2)


#6 sum of all number between given range
# sum=0
# a=int(input("enter your number"))
# for i in range(1,a):
#         sum=sum+a
# print(sum)


#7 sum of all number between given range
# sum=0
# a=int(input("enter your number"))
# for i in range(1,a):
#         if(i%2==1):
         
#          sum=sum+i
# print(sum)

#8  table
# a=int(input("enter a number"))
# for i in range(1,11):
#     print(a, " x ",i," = ",(a*i) )

#9 count number of digits in a number 
a=4567
sum=0
while a>0:
    a=a/10
    sum = sum+1

print(sum)
