class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val lookup = nums.toSet()

        var longest = 0
        for (num in nums) {
            if ((num - 1) !in lookup) {
                var current = 1
                while ((num + current) in lookup) {
                    current++
                }
                longest = maxOf(longest, current)
            }
        }

        return longest
    }
}
