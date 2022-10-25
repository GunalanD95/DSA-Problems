class Node:

    def __init__(self, val = None):
        self.left  = None
        self.right = None
        self.val = val



def isValidBST(root,bool_val):
    
    def dfs(node,minval,maxval,bool_val):
        if not node:
            return 
        if node.val > minval and node.val < maxval:
            bool_val = True
        else:
            bool_val = False
            
        left  = dfs(node.left,minval,node.val,bool_val)
        
        right = dfs(node.right,node.val,maxval,bool_val)

        print(left,right)
        if not left or not right:
            return False
    
        
        return bool_val
        
    min_val = float('-inf')
    max_val = float('inf')
    
    
    return dfs(root,min_val,max_val,bool_val)
    



if __name__ == '__main__':
    root = Node(5)
    n2 = Node(1)
    n3 = Node(4)
    n4 = Node(3)
    n5 = Node(6)
    root.left  = n2
    root.right = n3
    n3.left = n4 
    n3.right = n5
    bool_val = 1
    print("ValidBST",isValidBST(root,bool_val))
