class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            num1 = numbers[left]
            num2 = numbers[right]

            total = num1 + num2

            if total == target:
                return [left + 1, right + 1]

            if total < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]