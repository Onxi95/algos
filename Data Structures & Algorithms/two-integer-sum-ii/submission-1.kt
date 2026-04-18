class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left = 0
        var right = numbers.size - 1

        while (left < right) {
            val lower = numbers[left]
            val higher = numbers[right]
            val sum = lower + higher
            when {
                sum == target -> return intArrayOf(left + 1, right + 1)
                sum < target -> left++
                sum > target -> right--
            }
        }
        return intArrayOf(-1, -1)
    }
}
