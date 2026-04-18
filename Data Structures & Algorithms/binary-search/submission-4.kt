class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1

        while (left <= right) {
            val mid = (left + right) / 2
            val midGuess = nums[mid]
            when {
                midGuess == target -> return mid
                midGuess < target -> left = mid + 1
                midGuess > target -> right = mid - 1
            }
        }

        return -1
    }
}
