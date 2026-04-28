class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val len = nums.size
        val prefix = IntArray(len) { 1 }
        val postfix = IntArray(len) { 1 }
        val result = IntArray(len) { 0 }

        for (i in 1 until len) {
            prefix[i] = prefix[i - 1] * nums[i - 1]
        }

        for (i in len - 2 downTo 0) {
            postfix[i] = postfix[i + 1] * nums[i + 1]
        }

        for (i in 0 until len) {
            result[i] = prefix[i] * postfix[i]
        }

        return result
    }
}
