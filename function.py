def fun(name):   #defining a function
    print(f"good morning : {name}")
    return 0
name = "krish"
name2 = "sanuu"
name3= "rammu"
fun(name)
fun(name2)
fun(name3)

#add function
def add(num1,num2):
    result=num1+num2
    return result
a=45
b=34
c=add(a,b)
print(f"sum of {a} and {b} is : ",c)