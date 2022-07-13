
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

    
class BST:

    def __init__(self,val):
        self.root = Node(val)


    def preorder(self,root):
        if not root:
            return

        print("value",root.val)
        if root.left: self.preorder(root.left)
        if root.right: self.preorder(root.right)

    def noderange(self,root,B,C):
        stack = []
        def preorders(root,B,C):
            if not root:
                return

            print("value",root.val)
            if root.val >= B and root.val <= C: stack.append(root.val)
            if root.left: preorders(root.left,B,C)
            if root.right: preorders(root.right,B,C)
        preorders(root,B,C)

        return stack


# create a binary tree with the following structure:
# 1 ( root)
# 2  3 4  5
# 6 7 8 9 10

bt = BST(1)

bt.root.left = Node(2)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

bt.root.right = Node(3)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)


bt.root.right = Node(3)





# traversals

print(bt.preorder(bt.root))


print(bt.noderange(bt.root,12,20))