a = [4,5,6]
b = [11,12,15,17]

def merge(a,b):
	len_a = len(a)
	len_b = len(b)

	ai = 0
	bi = 0

	i = 0
	res = []
	while i < len_a + len_b:
		if ai < len_a and bi < len_b:
			if a[ai]< b[bi]:
				res.append(a[ai])
				ai+=1
			else:
				res.append(b[bi])
				bi+=1
		elif ai < len_a :
			res.append(a[ai])
			ai+=1
		elif bi < len_b :
			res.append(b[bi])
			bi+=1
		i+=1
	print "merge ",res,a,b
	return res	

def mergesort(data):
	print data,len(data)
	len_data = len(data)
	if len_data == 1:
		return data
	a = data[0:len_data/2]
	b = data[len_data/2:]
	resa = mergesort(a)
	resb = mergesort(b)
	res = merge(resa,resb)
	
	print "mergesort",res,"data ",data
	return res
	
res = []
res = mergesort([11,2,1,3,5,6])
print res