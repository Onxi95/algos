import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            mid = (left + right) // 2
            can_eat = self.can_eat_in_the_rate(piles, mid, h)
            if can_eat:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        
    def can_eat_in_the_rate(self, piles: List[int], current_rate: int, max_h: int) -> bool:
        time = 0
        for pile in piles:
            time += math.ceil(pile / current_rate)

        return time <= max_h