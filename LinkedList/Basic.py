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
            
            
ll = LL()
print("LinkedList",ll)
ll.insertfront(5)
ll.insertfront(10)
print("head",ll.head.data)
ll.insertend(25)
ll.insertend(35)
print(ll.insertpos(2,20))
print(ll.length())
