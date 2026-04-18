class Solution {
    fun trap(height: IntArray): Int {
        var prefixArray = MutableList<Int>(height.size) { 0 }
        var postfixArray = MutableList<Int>(height.size) { 0 }

        for (i in 1..(height.size - 1)) {
            prefixArray[i] = max(prefixArray[i - 1], height[i - 1])
        }

        for (i in height.size - 2 downTo 1) {
            postfixArray[i] = max(postfixArray[i + 1], height[i + 1])
        }

        val result = prefixArray.mapIndexed { index, prefix ->
            val postfix = postfixArray[index]
            max(0, min(postfix, prefix) - height[index])
        }

        return result.sum()
    }
}
