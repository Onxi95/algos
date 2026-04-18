# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        return bool(self.findSimilarRoot(root, subRoot))
        
    def findSimilarRoot(self, root: Optional[TreeNode], subRoot: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == subRoot.val:
            is_exact = self.isExactSubTree(root, subRoot)
            if is_exact:
                return subRoot
        
        return self.findSimilarRoot(root.left, subRoot) or self.findSimilarRoot(root.right, subRoot)

    def isExactSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isExactSubTree(root.left, subRoot.left) and self.isExactSubTree(root.right, subRoot.right)
        
        return False