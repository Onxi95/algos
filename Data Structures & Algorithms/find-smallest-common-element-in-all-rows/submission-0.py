class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common_elements = set(mat[0]).intersection(*mat[1:])
        return min(common_elements) if len(common_elements) >= 1 else -1