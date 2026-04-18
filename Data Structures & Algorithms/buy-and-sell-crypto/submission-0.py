class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]

            if buy < sell:
                potential_profit = sell - buy
                max_profit = max(potential_profit, max_profit)
            else:
                left = right
            right += 1

        return max_profit