import sys
#
# v1 -> v2 -> v3 -> v4
#
g = [   [0,10, 1, 1],
        [0, 0,10, 3],
        [0, 0, 0, 10],
        [0, 0, 0, 0],
        ]
def bellman(g):
    vsize = len(g)
    d = [sys.maxsize for i in range(vsize)]
    d[0] = 0
    for i in range(vsize):
        for j in range(vsize):
            if i!=j:
                #print(i,j,d[j], d[i] + g[i][j])
                if d[j] > d[i] + g[i][j]:
                    d[j] = d[i] + g[i][j]
                    print("after",i,j,d[i],d[j])

    print(d[vsize-1])
    print(d)

bellman(g)    
