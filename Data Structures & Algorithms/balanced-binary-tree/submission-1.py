# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced_l, left = self.getHeight(root.left if root else None)
        balanced_r, right = self.getHeight(root.right if root else None)

        return balanced_l and balanced_r and abs(left - right) <= 1
        
    def getHeight(self, root: Optional[TreeNode], h: int = 0) -> [bool, int]:
        if not root:
            return [True, h]

        balanced_l, left = self.getHeight(root.left, h + 1)
        balanced_r, right = self.getHeight(root.right, h + 1)
        is_balanced = balanced_l and balanced_r and abs(left - right) <= 1

        return [is_balanced, max(left, right)]
