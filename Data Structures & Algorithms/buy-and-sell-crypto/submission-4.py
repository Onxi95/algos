class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                buy = prices[i]
                sell = prices[j]
                diff = sell - buy
                max_profit = max(diff, max_profit)

        return max_profit    