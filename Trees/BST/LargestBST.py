'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
from collections import deque
class Node:

    def __init__(self, val = None):
        self.left  = None
        self.right = None
        self.val = val

def LargestBST(root):
    global ans 
    ans = []
    def postord(node):
        if not node:
            return
        postord(node.left)
        postord(node.right)
        ans.append(node.val)
        
    postord(root)
    print("ans",ans)




    


if __name__ == '__main__':
    root = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(3)
    n5 = Node(7)
    n6 = Node(18)
    root.left  = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    bool_val = 1
    print("LargestBST",LargestBST(root))