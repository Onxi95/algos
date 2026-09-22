# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float('inf')
        smallest = root

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                current_diff = abs(target - node.val)
                if current_diff < diff:
                    diff = current_diff
                    smallest = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return smallest.val if smallest else -1