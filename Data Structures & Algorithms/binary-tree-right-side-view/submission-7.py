# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            curr_size = len(queue)
            inner_result = []
            for i in range(curr_size):
                item = queue.pop(0)
                if item:
                    inner_result.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            if inner_result:
                result.append(inner_result[-1])

        return result