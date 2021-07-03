def partition(a,left,right):
    pivot = a[right]
    j = left
    for i in range(left,right):
        if a[i] < pivot:
            a[i],a[j] = a[j],a[i]
            j+=1
    a[j],a[right] = a[right],a[j]
    return j
def quicksort(a,left,right):
    if right - left <= 0:
        return;
    idx = partition(a,left,right)
    quicksort(a, left, idx-1)
    quicksort(a, idx + 1,right)


def changearr(a):
    a[0] = 100

a=[1,2,3,5,4,3,2,1]
quicksort(a,0,len(a)-1)
print(a)
