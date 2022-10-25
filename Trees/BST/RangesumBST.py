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

def rangeSumBST(root,low,high):
    
    def dfs(node):
        total_sum = 0 
        if not node:
            return total_sum
        if node.val >= low and node.val <= high:
            total_sum += node.val
            
       
        
        left = dfs(node.left)
        right = dfs(node.right)
        

        print("left",left,node.val)
        print("right",right,node.val)

        total_sum += left
        total_sum += right
        
        return total_sum

    return dfs(root)


def rangeSumBSTT(root,low,high):
    q = deque()

    q.append(root)
    total_count = 0


    while q:
        node = q.popleft()

        if node.val >= low and node.val <= high:
            total_count += node.val

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


    return total_count


    


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
    print("rangeSumBST",rangeSumBST(root,7,15))