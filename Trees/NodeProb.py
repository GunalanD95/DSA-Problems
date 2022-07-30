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


def nodepathans(A):
    res = []

    def bfs(node,maxval):
        if not node: 
            return 

        if node.val >= maxval:
            maxval = node.val
            res.append(node.val) 

        if node.left:
            bfs(node.left,maxval)

        if node.right:
            bfs(node.right,maxval)


    bfs(A,A.val)

    return res



def nodetopath(A,B):
    stk = [] 
    global flag
    flag = False
    def preorder(node,k):
        if not node :
            return False

        stk.append(node.val)
        if node.val == k:
            flag = False
        
        if not flag:
            left = preorder(node.left,k)
        if not flag:
            right = preorder(node.right,k)

        if flag == False:
            print("stack",stk)
            stk.pop()


    preorder(A,B)

    return stk





t = BST(1)

t.root.left = Node(2)
t.root.left.left = Node(4)
t.root.left.right = Node(5)

t.root.right = Node(3)
t.root.right.left = Node(6)
t.root.right.right = Node(7)


# print("NODE PATH - BFS",nodepathans(t.root))

print("PATH TO GIVEN NODE",nodetopath(t.root,7))