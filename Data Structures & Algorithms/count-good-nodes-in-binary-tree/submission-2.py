# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(node: Optional['TreeNode'], max_val: float):
            nonlocal total
            if not node:
                return

            if node.val >= max_val:
                total += 1

            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))

        dfs(root, root.val)

        return total