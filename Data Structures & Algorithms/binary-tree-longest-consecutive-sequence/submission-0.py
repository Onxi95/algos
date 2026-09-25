# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: Optional[TreeNode], prev: int, count: int):
            nonlocal result
            if not node:
                return
            
            current = count + 1 if node.val - prev == 1 else 1
            left = dfs(node.left, node.val, current)
            right = dfs(node.right, node.val, current)
            result = max(result, current)
            return current

        dfs(root, 999999999, 1)

        return result