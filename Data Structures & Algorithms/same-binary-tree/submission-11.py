# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            i1 = q1.popleft()
            i2 = q2.popleft()

            if not i1 and not i2:
                continue

            if not i1 or not i2:
                return False
            
            if i1.val != i2.val:
                return False
            
            q1.append(i1.left)
            q1.append(i1.right)

            q2.append(i2.left)
            q2.append(i2.right)

        return True