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
        result = []
        while queue:
            last = None
            for _ in range(len(queue)):
                item = queue.popleft()
                if item:
                    queue.append(item.left)
                    queue.append(item.right)
                    last = item

            if last:
                result.append(last.val)

        return result

            