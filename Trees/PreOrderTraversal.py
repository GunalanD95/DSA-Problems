# Given a binary tree, return the preorder traversal of its nodes values.

# NOTE: Using recursion is not allowed.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

    
class BST:

    def __init__(self,val):
        self.root = Node(val)



def preorderTraversal(A):
    stk = []
    def recursivepreorder(node):
        if not node:
            return 
        stk.append(node.val)
        if node.left: recursivepreorder(node.left)
        if node.right: recursivepreorder(node.right)
    recursivepreorder(A)
    print("stack",stk)
    return stk


def iterpreorderTraversal(A):
    stk = []
    stk.append(A)

    while len(stk) != 0:
        node = stk.pop()
        if node:
            print("node",node.val)
        if node.right:
            stk.append(node.right)

        if node.left:
            stk.append(node.left)



t = BST(4)

t.root.left = Node(5)
t.root.left.left = Node(7)
t.root.left.right = Node(8)

t.root.right = Node(2)
t.root.right.left = Node(3)
t.root.right.right = Node(6)



# RECURSIVE PRE-ORDER TRAVERSAL :
# preorderTraversal(t.root)

# ITERATIVE PRE-ORDER TRAVERSAL :
print(iterpreorderTraversal(t.root))