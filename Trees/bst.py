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
        if root.left:
            self.preorder(root.left)

        if root.right:
            self.preorder(root.right)


    def inorder(self,root):
        if not root:
            return 

        if root.left:
            self.inorder(root.left)

        print(root.val)

        if root.right:
            self.inorder(root.right)


    def postorder(self,root):
        if not root:
            return 

        if root.left:
            self.inorder(root.left)

        if root.right:
            self.inorder(root.right)

        print(root.val)



t = BST(1)

t.root.left = Node(2)
t.root.left.left = Node(4)
t.root.left.right = Node(5)


t.root.right = Node(3)
t.root.right.left = Node(6)
t.root.right.right = Node(7)


print("preorder",t.preorder(t.root))
print("inorder",t.inorder(t.root))
print("postorder",t.inorder(t.root))