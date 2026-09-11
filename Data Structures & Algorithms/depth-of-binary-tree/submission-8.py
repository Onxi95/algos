# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        stack = deque([root])
        level = 0
    
        while stack:
            has_node = False
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node:
                    continue
                has_node = True

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            if has_node:
                level += 1

        return level