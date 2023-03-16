#bubble sort
def bubblesort(array):
    for i in range (len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
        print(f"For {i} : ",data)
data=[-1,4,454,-456]
print("The initial data is : ",data)
bubblesort(data)
print("Final sorted array : ",data)
