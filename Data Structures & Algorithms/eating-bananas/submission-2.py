from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1

        left = 1
        right = max(piles)

        current = max(piles)

        while left <= right:
            speed = (left + right) // 2
            if self.canEat(piles, speed, h):
                right = speed - 1
                current = min(current, speed)
            else:
                left = speed + 1

        return current

        
    def canEat(self, piles: List[int], speed: int, h: int) -> bool:
        total = 0
        for pile in piles:
            total += ceil(pile / speed)

        return total <= h