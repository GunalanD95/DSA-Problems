class stack:
    def __init__(self):
        self.stk = []
        
    def push(self,val):
        self.stk.append(val)
        
    def pop(self):
        if not self.isEmpty():
            return self.stk.pop()
        
    def top(self):
        if not self.isEmpty():
            return self.stk[-1]
        
    def addback(self,val):
        return self.stk.insert(0,val)
        
    def isEmpty(self):
        if len(self.stk) == 0:
            return True
            
    def getstack(self):
        return self.stk



s = stack()
s.push(1)
s.push(2)
s.push(5)
s.addback(0)
s.addback(-1)
print(s.stk)
print(s.top())


# Approach 1:
# Stack Implementation using Python List
# Basically we are using a list to implement a stack.
# We are using the list.append() method to add an element to the end of the list.
# We are using the list.pop() method to remove an element from the end of the list.
# We are using the list.pop(0) method to remove an element from the beginning of the list.
# We are using the list.insert(0,val) method to add an element to the beginning of the list.
# We are using the len(list) method to get the length of the list.
# We are using the list.index(val) method to get the index of the value in the list.
