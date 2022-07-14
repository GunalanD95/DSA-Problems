import sys

# increase the recursion limit
sys.setrecursionlimit(10000)


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
            self.postorder(root.left)

        if root.right:
            self.postorder(root.right)

        print(root.val)


    def iterpreorder(self):
        stack = []
        stack.append(self.root)

        while len(stack) != 0:
            node = stack.pop()
            print("val",node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    def iterinorder(self):
        stack = []
        cur_node = self.root
        while cur_node  or stack:   
            while cur_node != None:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            print("val",cur_node.val)

            cur_node = cur_node.right

    def findheight(self,root):
        if not root:
            return 0
        left_height = self.findheight(root.left)
        right_height = self.findheight(root.right)
        return max(left_height,right_height) + 1



    def nodecounts(self,root):
        stack = []

        def preorder(root):
            stack.append(1)
            if not root:
                return
            if root.left:
                preorder(root.left)

            if root.right:
                preorder(root.right)

        preorder(root)
        return len(stack)


    def nodecounts(self,root):
        if not root:
            return 0
        return 1 + self.nodecount(root.left) + self.nodecount(root.right)

    def nodecount(self,root):
        if not root:
            return 0
        leftcount = self.nodecount(root.left)
        rightcount = self.nodecount(root.right)
        return leftcount + rightcount + 1


    #  count the number of nodes in the tree in iterative way
    def itercount(self):
        if not self.root:
            return 0
        count = 0
        stack = []
        stack.append(self.root)
        while len(stack) != 0:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count
    


    def checksame(self,A,B):
        if A is None and B is None:
            return 1


        if A is None or B is None:
            return 0

        if A.val != B.val:
            return 0

        left = self.checksame(A.left,B.left)
        
        right = self.checksame(A.right,B.right)

        if left == 1 and right == 1:
            return 1
        else:
            return 0




    def ansemax(self):
        stack = []
        stack.append(self.root)
        res = []
        res.append(self.root.val)
        while stack:
            node = stack.pop()
            print("node value",node.val)
            if node.right:
                if node.val < node.right.val: 
                    res.append(node.right.val)
                stack.append(node.right)

            if node.left:
                if node.val < node.left.val: 
                    res.append(node.left.val)
                stack.append(node.left)

        return res




# steps for iterative inorder
# 1. push root to stack , make cur_node = root
# 2. while stack is not empty and current node is not None
# 3. when current node is not None , push it to stack and make cur_node = current node's left child
# 4. when current node is None , pop it from stack and print it's value
# 5. make cur_node = current node's right child
# 6. repeat steps 2-5 until stack is empty






t = BST(4)

t.root.left = Node(5)


t.root.right = Node(2)
t.root.right.left = Node(3)
t.root.right.right = Node(6)


w = BST(1)
w.root.left = Node(2)



w.root.right = Node(3)
w.root.right.left = Node(6)
w.root.right.right = Node(7)


# print("check same",checksame(t.root,t.root))

# print("recursive preorder",t.preorder(t.root))
# print("inorder",t.inorder(t.root))
print("postorder",t.postorder(t.root))

# print("iter preorder",t.iterpreorder())
# print("iter inorder",t.iterinorder())




# print("height",t.findheight(t.root))


# print("nodes",t.nodecount(t.root))
# print("nodes -iter",t.itercount())


print("ancesort node",t.ansemax())