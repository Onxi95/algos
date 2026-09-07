class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first_ptr = m - 1
        second_ptr = n - 1
        modify_ptr = m + n - 1

        while first_ptr >= 0 and second_ptr >= 0:
            if nums1[first_ptr] > nums2[second_ptr]:
                nums1[modify_ptr] = nums1[first_ptr]
                first_ptr -= 1
            else:
                nums1[modify_ptr] = nums2[second_ptr]
                second_ptr -= 1
    
            modify_ptr -= 1

        while second_ptr >= 0:
            nums1[modify_ptr] = nums2[second_ptr]
            modify_ptr -= 1
            second_ptr -= 1
            