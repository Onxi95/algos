class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        current_min = prices[0]
        max_profit = 0

        for right in range(1, len(prices)):
            if current_min > prices[right]:
                current_min = prices[right]
            else:
                buy = current_min
                sell = prices[right]
                diff = sell - buy
                max_profit = max(max_profit, diff)
                left = right

        return max_profit