# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False


        if self.compare_trees(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compare_trees(self, nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
        if not nodeA and not nodeB:
            return True
        
        if nodeA and nodeB and nodeA.val == nodeB.val:
            return self.compare_trees(nodeA.left, nodeB.left) and self.compare_trees(nodeA.right, nodeB.right)

        return False
