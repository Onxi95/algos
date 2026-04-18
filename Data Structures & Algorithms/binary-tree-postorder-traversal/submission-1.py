# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])

    def helper(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return result
        
        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)
        return result