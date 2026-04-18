# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])

    def helper(self, root: Optional[TreeNode], arr: List[int]):
        if not root:
            return arr
        
        arr.append(root.val)
        self.helper(root.left, arr)
        self.helper(root.right, arr)

        return arr