class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        for ((index, value) in nums.withIndex()) {
            val guess = target - value
            if (guess in map) {
                return intArrayOf(map.getValue(guess), index)
            }
            map[value] = index
        }
        
        return intArrayOf()
    }
}
