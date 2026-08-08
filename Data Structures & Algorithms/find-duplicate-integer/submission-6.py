class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        another_slow = 0
        while True:
            slow = nums[slow]
            another_slow = nums[another_slow]
            if slow == another_slow:
                return slow
        
        return -1