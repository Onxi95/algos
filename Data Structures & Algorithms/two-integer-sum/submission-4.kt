class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map: MutableMap<Int, Int> = mutableMapOf()
        for((index, num) in nums.withIndex()) {
            val diff = target - num
            if(map.containsKey(diff)) {
                return intArrayOf(map[diff]!!, index)
            }
            map[num] = index
        }
        return intArrayOf()
    }
}
