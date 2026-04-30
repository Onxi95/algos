class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()

        for (idx in nums.indices) {
            if (idx > 0 && nums[idx] == nums[idx - 1]) continue

            val num = nums[idx]
            var left = idx + 1
            var right = nums.lastIndex
            
            while (left < right) {
                val leftNum = nums[left]
                val rightNum = nums[right]

                val total = leftNum + num + rightNum

                when {
                    total == 0 -> {
                        result.add(listOf(leftNum, num, rightNum))
                        while (left < right && nums[left] == nums[left + 1]) left++
                        while (left < right && nums[right] == nums[right - 1]) right--
                        left++
                        right--
                    }
                    total < 0 -> left++
                    total > 0 -> right--
                }
            }
        }
        return result
    }
}
