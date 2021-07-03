# Definition for singly-linked list.
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildFromList(datalist):
    first = True
    root = None
    tail = None
    for node in datalist:
        #print(node,root)
        if first == True:
            root = ListNode(node)
            tail = root
            first = False
        else:
            tail.next = ListNode(node)
            tail = tail.next

    return root
def dump(node):
    print("dump")
    tmp = node
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next
data = [
        [1,4,5],
        [1,3,4],
        [2,6],
]

def buildFromdata(data):
    lists = []
    for row in data:
       n = buildFromList(row)
       lists.append(n)
       #print(n)
       #dump(n)
    return lists

lists = buildFromdata(data)
q = PriorityQueue()
for head in lists:
    t = head
    while t!=None:
        q.put(t.val)
        t = t.next



while q.empty() == False:
    print(q.get())