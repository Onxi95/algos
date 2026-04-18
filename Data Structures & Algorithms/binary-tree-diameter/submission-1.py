# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.getNodeMaxHeight(root.left)
        right = self.getNodeMaxHeight(root.right)
        diameter = left + right
        return max(diameter, self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right))

        
    def getNodeMaxHeight(self, root: Optional[TreeNode], height: int = 0) -> int:
        if not root:
            return height
        return max(self.getNodeMaxHeight(root.left, height + 1), self.getNodeMaxHeight(root.right, height + 1))
