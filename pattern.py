#num=int(input("Enter The number : "))
n=int(input("Enter the number : "))
#li = [1,3,3,4,5,5]
px=n
py=n
for i in range (1,n+1):
  for j in range ( 1,n*2):
    if j==px or j==py or i==n:
        print("*",end="")
    else:
        print(" ",end="")
py=-1
px=+1
print()
