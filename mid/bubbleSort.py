# Bubble Sort
def swap(arr,i,j):
	t = arr[i]
	arr[i] = arr[j]
	arr[j] = t
 
def bubbleSort(arr):
 
	for i in range(len(arr)-1,-1,-1):
		for j in range(0,i):
			if arr[j] > arr[j+1]:
				swap(arr,j,j+1)
 
 
l = [10, 9, 8, 7, 6, 5]
 
print(l)
bubbleSort(l)
print(l)