# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = deque([(root, root.val)])
        total = 0
        
        while stack:
            node, max_val = stack.popleft()
            if node.val >= max_val:
                total += 1

            if node.left:
                stack.append((node.left, max(max_val, node.val)))
            if node.right:
                stack.append((node.right, max(max_val, node.val)))

        return total