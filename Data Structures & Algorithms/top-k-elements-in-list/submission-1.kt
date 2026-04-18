class Solution {
    fun topKFrequent(list: IntArray, k: Int): IntArray {
        return (
            list.toList().groupingBy { it }.eachCount().entries.sortedByDescending { it.value }.take(k).map { it.key }
                .toIntArray())
    }
}
