class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_mappings = {num: index for index, num in enumerate(nums2)}
        result = [0] * len(nums1)
        for index, num in enumerate(nums1):
            result[index] = nums2_mappings[num]

        return result