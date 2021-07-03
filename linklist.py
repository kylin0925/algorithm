class node:
    n = 0
    next = None
        
class LinkList:
    head = None
    tail = None
    def __init__(self):
        
        return
    def addNode(self,node):
        
        if self.head == None:
            self.head = node
            self.tail = node           
            self.head.next = None
        else:
            if self.head.next == None:
                self.head.next = node                           
                self.tail = node
            else:
                self.tail.next = node
                self.tail = self.tail.next
                self.tail.next = None
            
    def dumplist(self):
        tmp = self.head
        while(tmp!=None):
            print tmp.n
            tmp = tmp.next
    def reverseList(self):
        print ' reverse list'
        new_tail = self.head
        self.head = self.head.next
        new_tail.next = None
        #print new_tail,self.head.n
        while self.head !=None:
            tmp = self.head
            self.head = self.head.next
            tmp.next = new_tail
            new_tail = tmp
            #print new_tail.n
        self.head = new_tail    
lst = LinkList()

for i in range(10):
    a = node()
    a.n = i
    #print i
    lst.addNode(a)

#lst.dumplist()

lst.reverseList()
lst.dumplist()