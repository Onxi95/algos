# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])
        result = []

        while stack:
            right = None
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node:
                    break
                right = node

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            if right:
                result.append(right.val)

        return result