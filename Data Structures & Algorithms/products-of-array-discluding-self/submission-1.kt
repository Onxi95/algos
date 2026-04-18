class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val prefix = IntArray(nums.size)
        prefix[0] = 1
        for (i in 1 until nums.size) {
            prefix[i] = prefix[i - 1] * nums[i - 1]
        }

        val postfix = IntArray(nums.size)
        postfix[nums.size - 1] = 1
        for (i in postfix.size - 2 downTo 0) {
            postfix[i] = postfix[i + 1] * nums[i + 1]
        }

        val result = IntArray(nums.size)
        for (i in 0 until nums.size) {
            result[i] = prefix[i] * postfix[i]
        }

        return result
    }
}
