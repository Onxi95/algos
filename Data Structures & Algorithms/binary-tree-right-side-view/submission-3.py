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

        result = [] 
        queue = deque([root])

        while queue:
            l = len(queue)
            last = None
            for index in range(l):
                item = queue.popleft()
                if item:
                    last = item
                    queue.append(item.left)
                    queue.append(item.right)
            if last:
                result.append(last.val)

        return result