class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while left < right and right < len(prices):
            if prices[left] < prices[right]:
                buy = prices[left]
                sell = prices[right]
                diff = sell - buy
                max_profit = max(max_profit, diff)
            else:
                left = right

            right += 1

        return max_profit