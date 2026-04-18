class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            prices_l = prices[left]
            prices_r = prices[right]

            if prices_l < prices_r:
                max_profit = max(max_profit, prices_r - prices_l)
            else:
                left = right

            right += 1

        return max_profit