class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()

        for ((index, num) in nums.withIndex()) {
            if (index > 0 && nums[index - 1] == num) continue

            var left = index + 1
            var right = nums.size - 1
            while (left < right) {
                val threeSum = num + nums[left] + nums[right]
                when {
                    threeSum > 0 -> right--
                    threeSum < 0 -> left++
                    threeSum == 0 -> {
                        result.add(listOf(num, nums[left], nums[right]))
                        left++
                        right--
                        while (left < right && nums[left] == nums[left - 1]) {
                            left++
                        }
                        while (left < right && nums[right] == nums[right + 1]) {
                            right--
                        }
                    }
                }
            }
        }

        return result
    }
}
