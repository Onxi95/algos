# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])

        right_view = []

        while queue:
            right_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right_node:
                right_view.append(right_node.val)

        return right_view