# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            inner_result = []

            for i in range(len(queue)):
                item = queue.popleft()
                if item:
                    inner_result.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            
            if inner_result:
                result.append(inner_result)

        return result

