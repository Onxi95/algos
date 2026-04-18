# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.countGoodNodes(root, root.val)

    def countGoodNodes(self, root: Optional[TreeNode], current_max: int) -> int:
        if not root:
            return 0

        current_count = 1 if root.val >= current_max else 0

        left = self.countGoodNodes(root.left, max(current_max, root.val))
        right = self.countGoodNodes(root.right, max(current_max, root.val))

        return current_count + left + right