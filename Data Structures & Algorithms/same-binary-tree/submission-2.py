# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for i in range(len(q1)):
                q1_item = q1.popleft()
                q2_item = q2.popleft()

                if q1_item is None and q2_item is None:
                    continue

                if q1_item is None or q2_item is None or q1_item.val != q2_item.val:
                    return False

                q1.append(q1_item.left)
                q1.append(q1_item.right)
                q2.append(q2_item.left)
                q2.append(q2_item.right)

        return True
        