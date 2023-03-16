def fec(n):
    if n==0 or n==1:
        return 1
    elif n<-1:
        print("Not define")
    else:
        return n*fec(n-1)

x=int(input("Enter The number : "))
fact=fec(x)
print(f"The factotial of {x} is : ",fact)
