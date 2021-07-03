A = [1,2,3,4,5,6,7,8,10,9]
arr_size = len(A)

# swap a,b = b,a
def swap(i,j):
	#print("swap",i,j)
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

def max_heapfy_old(i):
	
	#print arr_size
	if i*2 + 1 >= arr_size:
		l = None
	else:
		l = i*2 + 1
	if i*2 + 2 >= arr_size:
		r = None
	else:
		r = i*2 + 2
		
	#print i,l,r,A
	if l != None and A[i] < A[l]:
		if r == None:
			swap(i,l)
			max_heapfy(l)
		elif r!=None and A[l]>A[r]:
			swap(i,l)
			max_heapfy(l)
		elif r!=None and A[l]<A[r]:
			swap(i,r)
			max_heapfy(r)
	elif r!=None and A[i] < A[r]:
		if l == None:
			swap(i,r)
			max_heapfy(r)
		elif l!=None and A[l]>A[r]:
			swap(i,l)
			max_heapfy(l)
		elif l!=None and A[l]<A[r]:
			swap(i,r)
			max_heapfy(r)
	

def max_heapify(i):
	
    largest = i
    l = i*2 + 1
    r = i*2 + 2
    
	#max A[i] ,A[l], A[r]
    #print(i,l,r)
    if l < arr_size and A[i] < A[l]:
        largest = l       
    if r < arr_size and A[largest] < A[r]:
        largest = r
    if largest!=i :
        swap(i,largest)
        max_heapify(largest)		

	
for i in range(arr_size//2,-1,-1):
	max_heapify(i)	
	print(A)
print(" after heapify")
print(A)    
print("-------------------------------")
_arr_size = arr_size
for i in range(_arr_size):
	swap(0,arr_size-1)
	arr_size = arr_size-1
	print(A)
	
	
	max_heapify(0)
	print("count ",i," array ",A)
	#a=raw_input()
	