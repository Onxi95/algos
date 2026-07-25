class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * postfix[i]

        if nums.count(0):
            for i in range(len(nums)):
                if nums[i] != 0:
                    result[i] = 0
 
        return result