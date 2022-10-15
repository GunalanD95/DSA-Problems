from collections import deque 

class Solution:
	def levelOrder(self, root):
        if not root:
            return []

        ans = []

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            for i in range(size):
                cur_node = q.popleft()
                if cur_node:
                    q.append(cur_node.left)
                    q.append(cur_node.right)

                    level.append(cur_node.val)

            if level:
                ans.append(level)


        return ans 