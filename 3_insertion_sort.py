#insertion sort
from array import *
ar=array('i',[100])
n=int(input("Enter the size of array : "))
for i in range (1,n+1):
    a=int(input(f"Enter The {i} element : "))
    ar.append(a)
for k in range (1,n):
    temp=ar[k]
    j=k-1
    while temp>ar[j] & j>=0:
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=temp
print("Sorted array is : ")
for i in range (1,n+1):
    print(ar[i],end=" ")