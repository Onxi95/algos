import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxArea(heights: IntArray): Int {
        var left = 0
        var right = heights.lastIndex
        var maxArea = 0

        while (left < right) {
            val leftHeight = heights[left]
            val rightHeight = heights[right]
            
            val currentMinHeight = min(leftHeight, rightHeight)
            val base = right - left
            val currentArea = currentMinHeight * base

            maxArea = max(maxArea, currentArea)

            if (leftHeight > rightHeight) right-- else left++
        }

        return maxArea
    }
}