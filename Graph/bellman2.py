import sys
def bellman(G):
    size = len(G)
    distance = [sys.maxsize for i in range(size)]
    distance[0] = 0
    path = [sys.maxsize for i in range(size)]
    path[0] = 0
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if distance[j] > distance[i] + G[i][j]:
                    distance[j] = distance[i] + G[i][j]
                    # update path
                    path[j] = i

    print(distance)
    print(path)
    return distance[size -1]
         #         0             1         2            3         4              5
G = [   [          0,            5 ,   sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize],
        [sys.maxsize,            0 ,             6, sys.maxsize,          -4, sys.maxsize],
        [sys.maxsize,  sys.maxsize ,             0, sys.maxsize,          -3,          -2],
        [sys.maxsize,  sys.maxsize ,             4,           0, sys.maxsize, sys.maxsize],
        [sys.maxsize,  sys.maxsize ,   sys.maxsize,           1,           0,           6],
        [          3,             7,   sys.maxsize, sys.maxsize, sys.maxsize,           0],
    ]    
bellman(G)    