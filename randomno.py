import random
import numpy as np

n=int(input("enter an number of samples"))
a=2

n1=np.zeros(n)
for i in range(0,n):
    n1[i]=random.randint(1,50)

print(n1)    

s=0
for i in range(0,n):
    s=s+n1[i]

mean=s/n
print("mean",mean)

t=0
for i in range(0,n):
    for j in range(i+1,n):
        if(n1[i]>n1[j]):
            t=n1[i]
            n1[i]=n1[j]
            n1[j]=t
print(n1)

k=n/2
if(k%2!=0):
    median=n[k]

# median=np.median(n1)
# print("median",median)


