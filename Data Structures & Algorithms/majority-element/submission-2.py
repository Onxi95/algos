class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        majority = nums[0]
        current = 1

        for num in nums[1:]:
            if num == majority:
                current += 1
            else:
                current -= 1

                if current == 0:
                    majority = num
                    current = 1
        
        return majority