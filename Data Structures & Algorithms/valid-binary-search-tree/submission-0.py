# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.validateNodes(root)

    def validateNodes(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        if not root:
            return True

        if not (left < root.val < right):
            return False

        return self.validateNodes(root.left, left, root.val) and self.validateNodes(root.right, root.val, right)
