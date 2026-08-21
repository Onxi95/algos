# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        current = self.findDepth(root.left) + self.findDepth(root.right)
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)

        return max(current, left, right)

    def findDepth(self, root: Optional[TreeNode], depth = 0):
        if not root:
            return depth

        return max(self.findDepth(root.left, depth + 1), self.findDepth(root.right, depth + 1))