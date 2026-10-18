class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        zeros = nums.count(0)
        if zeros >= 2:
            return [0] * n

        prefix = [0] * n
        postfix = [0] * n
        result = [0] * n
        prefix[0] = postfix[-1] = 1

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(n):
            result[i] = postfix[i] * prefix[i]
        return result