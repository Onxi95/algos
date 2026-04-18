# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        self.result = -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        self.count = k
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root or self.result != -1:
            return
        
        self.dfs(root.left)
        
        if self.result == -1:
            self.count -= 1
            if self.count == 0:
                self.result = root.val
                return

        self.dfs(root.right)
