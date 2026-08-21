# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.helper(node, subRoot):
                return True

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return False

        
    def helper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q1 = deque([root])
        q2 = deque([subRoot])

        while q1 and q2:
            p1 = q1.popleft()
            p2 = q2.popleft()

            if not p1 and not p2:
                continue

            if not p1 or not p2 or p1.val != p2.val:
                return False
            
            q1.append(p1.left)
            q1.append(p1.right)
            q2.append(p2.left)
            q2.append(p2.right)

        return not q1 and not q2