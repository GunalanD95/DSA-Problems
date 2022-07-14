
from operator import invert
from turtle import right


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

        print("value preorder",root.val)
        if root.left: self.preorder(root.left)
        if root.right: self.preorder(root.right)

    def noderange(self,root,B,C):
        stack = []
        def preorders(root,B,C):
            if not root:
                return

            print("value noderange",root.val)
            if root.val >= B and root.val <= C: stack.append(root.val)
            if root.left: preorders(root.left,B,C)
            if root.right: preorders(root.right,B,C)
        preorders(root,B,C)

        return stack

    def nodepath(self,k):
        self.stack = []
        self.targetfound = False
        def inordpath(root,k):
            if not root: 
                return False

            self.stack.append(root.val)

            if not self.targetfound:
                left = inordpath(root.left,k)

            print("value nodepath",root.val)
            
            print("stack",self.stack)

            if root.val == k:
                print("Value Found",root.val)
                self.targetfound = True
                return True 


            if not self.targetfound:
                right = inordpath(root.right,k)

            if not self.targetfound:
                print("stack -L-R",self.stack)
                self.stack.pop()
            if left == True or  right == True:
                return True

        inordpath(self.root,k)


        return self.stack


# Write the approach for above function inordpath as below:

# steps for path to a given node:
# 1. create a stack and boolean variable targetfound
# 2. use inorder traversal to traverse the tree only if the target is not found
# 3. if the target is found, set targetfound to true
# 4. if the target is not found, pop the last element from the stack
# 5. if the target is not found, return false



        



    def inverttree(self,root):
        if root == None:
            return 
        else:
            # temp = root
            # print(temp.val)
            temp = root.left
            root.left = root.right
            root.right = temp

            self.inverttree(root.left)
            self.inverttree(root.right)




            




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







# traversals

# print(bt.preorder(bt.root))


# print(bt.noderange(bt.root,12,20))

# print(bt.inverttree(bt.root))

# print(bt.preorder(bt.root))


print("node path",bt.nodepath(5))