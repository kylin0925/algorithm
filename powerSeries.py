print("acm766")
def c(n,k):        
    tmp = 1
    i=1
    while k > 0:
        tmp *=n
        tmp//=i        
        k-=1
        n-=1
        i+=1
        #print(tmp)
    #print(tmp)
    return tmp
def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)
def lcm(n,m):
    return m*n // gcd(n,m)

#build pascal table for (n+1)^k
table = [[1],[1,1]]
for k in range(2,22):
    tmp = []
    for i in range(k+1):
        tmp.append(c(k,i))
    table.append(tmp)

# S_k = 1^k + 2^k + 3^k + .... + n^k 
# pre-caculate for S_0, S_1, S_2
res_table = [[0,1],[0,1,1],[0,1,3,2]]
d_table = [1,2,6]

#  
# i^k , i=1 to n
# n^(k+1) 
#

#k=3 # i^k , i=1 to n

def solv_sum_power(k):
    global res_table
    global d_table
    global table
    right = table[k+1][:]
    left = table[k+1][:]
    left[0] = 0
    left[1] -=1
    #print(left,right)

    # 1 ~ k - 1 lcm
    dlcm = 1
    for i in range(1,k):
        #print(d_table[i],res_table[i])
        dlcm = lcm(dlcm,d_table[i])

    #print(dlcm)

    left = [dlcm * x for x in left]
    #print("left",left)

    for i in range(1,k):
        right[i] = (dlcm * right[i])// d_table[i] 

    right[k] = (dlcm * right[k])
    #print("right",right)

    for i in range(1,k):
        tmp = res_table[i][:]
        tmp = [ right[i] * x for x in tmp ]
        #print("tmp",tmp)
        for j in range(len(tmp)):
            left[j] -=tmp[j]

    m = right[k]
    for n in left:
        m = gcd(m,n)
    left = [x//m for x in left]    
    #print("num ",k,right[k]//m,left)
    d_table.append(right[k]//m)
    res_table.append(left)

for k in range(3,21):
    solv_sum_power(k)
    print("k",k,d_table[k],res_table[k])