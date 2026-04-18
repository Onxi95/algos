# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            queue_length = len(queue)
            inner_result = []
            for _ in range(queue_length):
                item = queue.popleft()
                if item:
                    inner_result.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            if inner_result:
                result.append(inner_result)

        return result