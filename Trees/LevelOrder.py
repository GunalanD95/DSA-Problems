from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

    

def levelorder(node):
    if not node:
        return 
    ans = []
    q = deque()
    q.append(node)
    while q:
        for i in range(len(q)):
            cur_node = q.popleft()
            level = []
            if cur_node:
                q.append(cur_node.left)
                q.append(cur_node.right)
                print(cur_node)
                level.append(cur_node.val)
        if level:
            ans.append(level)
    return ans 

def constructbt(arr):
    root = TreeNode(arr[0])

    q = deque()
    q.append(root)
    
    indx = 1
    while q and indx < len(arr):
        cur_node = q.popleft()

        left_node = None 
        if A[indx] != -1:
            left_node = TreeNode(A[indx])
            q.append(left_node)

        indx += 1
        right_node = None
        if A[indx] != -1:
            right_node = TreeNode(A[indx])
            q.append(right_node)

        cur_node.left = left_node
        cur_node.right = right_node 
    return root 


A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
BST = constructbt(A)
print("new-tree",BST)

print("level-order",levelorder(BST))


