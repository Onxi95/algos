# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root: Optional[TreeNode], depth = 0) -> int:
        if not root:
            return depth

        return max(self.getHeight(root.left, depth + 1), self.getHeight(root.right, depth + 1))