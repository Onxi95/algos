class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()

        return buildList {
            for ((idx, num) in nums.withIndex()) {
                if (idx > 0 && num == nums[idx - 1]) continue

                var left = idx + 1
                var right = nums.lastIndex

                while (left < right) {
                    val total = nums[left] + num + nums[right]

                    when {
                        total == 0 -> {
                            add(listOf(nums[left], num, nums[right]))
                            do { left++ } while (left < right && nums[left] == nums[left - 1])
                            do { right-- } while (left < right && nums[right] == nums[right + 1])
                        }
                        total < 0 -> left++
                        else -> right--
                    }
                }
            }
        }
    }
}
