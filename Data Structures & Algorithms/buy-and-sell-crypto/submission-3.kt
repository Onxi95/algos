import kotlin.math.max

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var currentLow = prices[0]
        var currentTotal = 0

        for (i in 1..prices.lastIndex) {
            val current = prices[i]

            if (current < currentLow) {
                currentLow = current
            } else {
                currentTotal = max(currentTotal, current - currentLow)
            }
        }

        return currentTotal
    }
}
