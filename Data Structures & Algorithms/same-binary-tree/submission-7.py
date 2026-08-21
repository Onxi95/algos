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

            if p1 and p2 and p1.val != p2.val:
                return False

            p1left = p1.left.val if p1 and p1.left else None
            p1right = p1.right.val if p1 and p1.right else None

            p2left = p2.left.val if p2 and p2.left else None
            p2right = p2.right.val if p2 and p2.right else None

            if p1left != p2left or p1right != p2right:
                return False

            if p1:
                q1.append(p1.left)
                q1.append(p1.right)
            if p2:
                q2.append(p2.left)
                q2.append(p2.right)

        return len(q1) == len(q2)