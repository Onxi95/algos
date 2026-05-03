import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxArea(heights: IntArray): Int {
        var left = 0
        var right = heights.lastIndex

        var maxArea = 0

        while (left < right) {
            val currentMinHeight = min(heights[left], heights[right])
            val base = right - left
            val currentArea = currentMinHeight * base
            maxArea = max(maxArea, currentArea)

            when {
                heights[left] > heights[right] -> right--
                heights[left] < heights[right] -> left++
                else -> left++
            }
        }

        return maxArea
    }
}