class Solution {
    fun topKFrequent(
        nums: IntArray,
        k: Int,
    ): IntArray {
        val counts = nums.toList().groupingBy { it }.eachCount()
        val buckets = List(nums.size + 1) { mutableListOf<Int>() }

        for ((num, count) in counts) {
            buckets[count].add(num)
        }

        val result = mutableListOf<Int>()

        for (i in buckets.size - 1 downTo 1) {
            for (possible in buckets[i]) {
                result.add(possible)
                if (result.size == k) {
                    return result.toIntArray()
                }
            }
        }

        return intArrayOf()
    }
}
