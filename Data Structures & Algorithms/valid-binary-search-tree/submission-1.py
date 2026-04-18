# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isValidSubTree(root, float('-inf'), float('inf'))

    def isValidSubTree(self, node: Optional[TreeNode], left: float, right: float) -> bool:
        if not node:
            return True

        current = node.val

        if not (left < node.val < right):
            return False

        return self.isValidSubTree(node.left, left, node.val) and self.isValidSubTree(node.right, node.val, right)