#Selection Sort
 
def swap(l,i,j):
	t = l[i]
	l[i] = l[j]
	l[j] = t
 
def smallestIndex(l,low,high):
	smallesti = low
	for i in range(low+1,high+1):
		if l[i] < l[smallesti]:
			smallesti = i
	return smallesti
 
def selectionSort(l):
	for i in range(len(l)):
		j = smallestIndex(l,i,len(l)-1)
		swap(l,i,j)
 
l = [5,7,19,4,10,1]
 
print(l)
 
selectionSort(l)
 
print(l)
 
 