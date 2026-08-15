from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.memory = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memory[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        val = self.memory[key]
        if not val:
            return ""

        left = 0
        right = len(val) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if val[mid][0] <= timestamp:
                result = val[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result