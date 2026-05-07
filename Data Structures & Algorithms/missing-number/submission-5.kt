class Solution {
    fun missingNumber(nums: IntArray): Int {
        var res = 0
        for (i in 0..nums.size) {
            res = res xor i
        }
        for (i in nums) {
            res = res xor i
        }

        return res
    }
}
