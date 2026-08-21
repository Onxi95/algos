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
        
        diameter = 0

        def get_depth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            left = get_depth(node.left)
            right = get_depth(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        get_depth(root)
        return diameter