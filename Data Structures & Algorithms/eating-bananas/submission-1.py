class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        if len(piles) == h:
            return largest
        
        left = 1
        right = largest
        result = largest

        while left <= right:
            current_time = 0
            mid = (left + right) // 2
            for pile in piles:
                current_time += math.ceil(pile / mid)
            
            if current_time <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result