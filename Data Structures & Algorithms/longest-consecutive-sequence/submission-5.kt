import kotlin.math.max

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val uniques = nums.toSet()
        var longest = 0

        for (unique in uniques) {
            var currentLongest = 1
            var prev = unique - 1
            while (prev in uniques) {
                currentLongest++
                prev--
            }
            
            longest = max(longest, currentLongest)
        }

        return longest
    }
}
