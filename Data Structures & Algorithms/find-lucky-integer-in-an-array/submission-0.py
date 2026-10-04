from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        result = -1
        for key, value in count.items():
            if key == value and value > result:
                result = value
        return result