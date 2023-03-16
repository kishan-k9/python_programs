# Selection_sort
def selectionSort(array):
	for i in range(len(array)):
		min = i
		for j in range(i + 1,len(array)):
			# select the minimum element in every iteration
			if array[j] < array[min]:
				min = j
		# swapping the elements to sort the array
		(array[i], array[min]) = (array[min], array[i])
      #  print(f"For {i} : ",data)
data = [45,23,4543,5,47,98,0]
selectionSort(data)
print('Final sorted array is :',data)