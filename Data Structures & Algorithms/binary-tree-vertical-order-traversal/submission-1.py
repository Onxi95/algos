# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cols = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            cols[index].append(node.val)
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))

        return [cols[col] for col in sorted(cols)]