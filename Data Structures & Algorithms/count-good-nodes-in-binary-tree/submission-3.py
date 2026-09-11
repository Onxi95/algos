# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional['TreeNode'], max_val: float):
            if not node:
                return 0

            count = 0

            if node.val >= max_val:
                count += 1

            count += dfs(node.left, max(max_val, node.val))
            count += dfs(node.right, max(max_val, node.val))

            return count

        return dfs(root, root.val)