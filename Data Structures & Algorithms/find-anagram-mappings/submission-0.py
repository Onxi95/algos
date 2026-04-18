class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen_indexes = {}
        for index, num in enumerate(nums2):
            seen_indexes[num] = index
        
        result = []

        for num in nums1:
            result.append(seen_indexes[num])

        return result