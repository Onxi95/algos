class Solution {
    fun topKFrequent(list: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        val freq = List(list.size + 1) { mutableListOf<Int>() }
        list.forEach { map[it] = map.getOrPut(it) { 0 } + 1 }

        map.forEach { (value, count) -> freq[count].add(value) }

        val result = mutableListOf<Int>()

        for (i in freq.size - 1 downTo 1) {
            for (num in freq[i]) {
                result.add(num)

                if (result.size == k) {
                    return result.toIntArray()
                }
            }
        }
        return intArrayOf()
    }
}
