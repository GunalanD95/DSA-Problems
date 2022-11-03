'''
Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree 
and right subtree.
'''

class Node:

    def __init__(self, val = None):
        self.left  = None
        self.right = None
        self.val = val

def preOrder(node):
    if not node:
        return 

    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

def CheckSum(root):
    def checLeafNode(node):
        if not node.left and not node.right:
            return False
        return True

    def dfs(node):
        if not node:
            return 0

        left  = dfs(node.left)
        right = dfs(node.right)

        print(left+right,node.val)
        if checLeafNode(node):
            if node.val == left + right:
                pass
            else:
                return 0

        return node.val + left + right

    value = dfs(root)
    return 0 if value == 0 else 1





    


if __name__ == '__main__':
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(3)
    root.left  = n2
    root.right = n3
    n3.left = n4
    n4.right = n5
    print("CheckSum",CheckSum(root))