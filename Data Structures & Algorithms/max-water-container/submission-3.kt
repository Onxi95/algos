class Solution {
    fun base(i: Int, j: Int): Int = j - i
    fun height(heights: IntArray, i: Int, j: Int): Int = min(heights[i], heights[j])

    fun getCurrentArea(heights: IntArray, i: Int, j: Int): Int = base(i, j) * height(heights, i, j)

    fun maxArea(heights: IntArray): Int {
        if (heights.size < 2) throw IllegalArgumentException("Array size must be larger than 1")
        var left = 0
        var right = heights.size - 1
        var largestArea = 0

        while (left < right) {
            largestArea = max(getCurrentArea(heights, left, right), largestArea)
            val leftHeight = heights[left]
            val rightHeight = heights[right]
            when {
                leftHeight < rightHeight -> left++
                leftHeight > rightHeight -> right--
                else -> left++
            }
        }

        return largestArea
    }
}
