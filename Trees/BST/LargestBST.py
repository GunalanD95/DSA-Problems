'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
class Node:

    def __init__(self, val = None):
        self.left  = None
        self.right = None
        self.val = val


class TreeNode:

    def __init__(self,min_node,max_node,max_size):
        self.min_node  = min_node
        self.max_node = max_node
        self.max_size = max_size

def LargestBST(root):
    def postord(node):
        if not node:
            return TreeNode(float('inf'),float('-inf'),0)
        
        left = postord(node.left)
        right = postord(node.right)

        # if bst
        if left.max_node < node.val and right.min_node > node.val:
            return TreeNode(min(left.min_node,node.val),max(right.max_node,node.val)
                            ,left.max_size + right.max_size + 1)


        # if its not a BST then return 

        return TreeNode(float('-inf'),float('inf'),max(left.max_size,right.max_size))

    return postord(root).max_size




    


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