class Solution {
    fun isAnagram(first: String, second: String): Boolean {
        if (first.length != second.length) return false
        return first.groupBy { it } == second.groupBy { it }
    }
}
