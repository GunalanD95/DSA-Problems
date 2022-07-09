class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LL:
    def __init__(self):
        self.head = None
  
    def insertfront(self,data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
            print("new head",self.head.data)
        else:
            self.head = newNode
            print("head",self.head.data)
            
    def insertend(self,data):
        newNode = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        
            
    def length(self):
        temp = self.head
        c = 0
        while temp:
            print("ll data",temp.data,"pos",c)
            c += 1
            temp = temp.next
        return c
        
    def insertpos(self,pos,data):
        newNode = Node(data)
        c = 0
        temp = self.head
        while c < pos -1:
            print("printval",temp.data,c)
            temp = temp.next
            c += 1
        newNode.next = temp.next
        temp.next = newNode
        
    def delete(self,pos):
        temp = self.head
        if pos == 0:
            newhead = temp.next
            self.head = newhead
            print('delete head')
        else:
            c = 0 
            while c < pos-1:
                print("del",temp.data,c)
                temp = temp.next
                c += 1
            print("del before",temp.data)
            newval = temp.next.next
            temp.next = newval
        
    def printll(self):
        temp = self.head
        while temp:
            print("printing--",temp.data)
            temp = temp.next
            
ll = LL()
print("LinkedList",ll)
ll.insertfront(5)
ll.insertfront(10)
ll.insertfront(100)
ll.insertend(25)
ll.insertend(35)
ll.insertpos(2,20)
print("before deletion",ll.printll())
print("delete print",ll.delete(3))
print(ll.printll())