# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        queue = deque([root])
        result = []

        while queue:
            for i in range(len(queue)):
                item = queue.popleft()
                if item:
                    result.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
        
        result.sort()
        if k > 0 and k <= len(result):
            return result[k - 1]
        return -1