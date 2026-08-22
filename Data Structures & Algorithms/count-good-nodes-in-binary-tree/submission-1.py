# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0

        def dfs(root, curr_max):
            nonlocal total
            if not root:
                return

            if curr_max <= root.val:
                total += 1
            dfs(root.left, max(curr_max, root.val))
            dfs(root.right, max(curr_max, root.val))

        dfs(root, float('-Infinity'))
        return total