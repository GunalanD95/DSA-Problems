'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
class Node:

    def __init__(self, val = None):
        self.left  = None
        self.right = None
        self.val = val


def getMaxDepth(root):
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        return max(left,right) + 1 

    return dfs(root)



    


if __name__ == '__main__':
    root = Node(10)
    n2 = Node(5)
    n3 = Node(15)
    n4 = Node(3)
    n5 = Node(7)
    n6 = Node(18)
    n7 = Node(2)
    n8 = Node(1)
    root.left  = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    n4.left = n7
    n7.left = n8
    print("getMaxDepth",getMaxDepth(root))