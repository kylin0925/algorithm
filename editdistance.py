def editdistance(a,b):
    alen = len(a)
    blen = len(b)
    dmap = [ [0 for i in range(alen+1)] for j in range(blen+1)  ]

    for i in range(alen+1):
        dmap[0][i] = i

    for i in range(blen + 1):
        dmap[i][0] = i

    for i in range(1,blen+1):
        for j in range(1,alen+1):
            if a[j-1] == b[i-1]:
                dmap[i][j] = dmap[i-1][j-1]
            else:
                dmap[i][j] = min(dmap[i - 1][j] +1,dmap[i][j-1] +1,dmap[i - 1][j-1]+1)


    for r in dmap:
        print(r)
    print(dmap[blen][alen])
editdistance("134","12")