# Given a binary tree, return the postorder Traversal  of its nodes values.

# NOTE: Using recursion is not allowed.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

    
class BST:

    def __init__(self,val):
 
 
        self.root = Node(val)

    def postorder(self,node):
        if not node:
            return 

        if node.left:
            self.postorder(node.left)

        if node.right:
            self.postorder(node.right)


        print(node.val)






t = BST(4)

t.root.left = Node(5)
t.root.left.left = Node(7)
t.root.left.right = Node(8)

t.root.right = Node(2)
t.root.right.left = Node(3)
t.root.right.right = Node(6)

# RECURSIVE POST ORDER TRAVERSAL
# print(recpost(t.root))

print("NODE PATH - BFS",t.postorder(t.root))