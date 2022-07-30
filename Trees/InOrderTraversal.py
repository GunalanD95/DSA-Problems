# Given a binary tree, return the inorder traversal  of its nodes values.

# NOTE: Using recursion is not allowed.

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

    
class BST:

    def __init__(self,val):
        self.root = Node(val)



def inorderTraversal(node):
    if not node:
        return 

    if node.left: inorderTraversal(node.left)
    print("inorder-node",node.val)
    if node.right: inorderTraversal(node.right)

def iterinorderTraversal(A):
    stk = []
    node = A
    while stk or node:
        while node != None:
            stk.append(node)
            node = node.left
        node = stk.pop()
        print("node-val",node.val)
        node = node.right


t = BST(4)

t.root.left = Node(5)
t.root.left.left = Node(7)
t.root.left.right = Node(8)

t.root.right = Node(2)
t.root.right.left = Node(3)
t.root.right.right = Node(6)


# RECURSIVE INORDER TRAVERSAL
# print(inorderTraversal(t.root))

# ITERATIVE INORDER TRAVERSAL
print(iterinorderTraversal(t.root))