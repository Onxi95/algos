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
            p1 = q1.popleft()
            p2 = q2.popleft()

            if not p1 and not p2:
                continue

            if p1 is None or p2 is None or p1.val != p2.val:
                return False

            q1.append(p1.left)
            q1.append(p1.right)
            q2.append(p2.left)
            q2.append(p2.right)

        return True