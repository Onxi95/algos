class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[len(nums1) - 1 - i] = nums2[i]

        for i in range(m, m + n):
            index = i
            while index > 0 and nums1[index] < nums1[index - 1]:
                nums1[index], nums1[index - 1] = nums1[index -1], nums1[index]
                index -= 1
        