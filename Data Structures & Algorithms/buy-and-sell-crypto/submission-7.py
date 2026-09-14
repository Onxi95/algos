class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1

        result = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            diff = sell - buy

            result = max(diff, result)

            if sell < buy:
                left = right

            right += 1


        return result