class Solution {
    fun isAnagram(first: String, second: String): Boolean {
        if (first.length != second.length) {
            return false
        }
        val firstLetters = first.groupingBy { it }.eachCount()
        val secondLetters = second.groupingBy { it }.eachCount()
        println("$firstLetters | $secondLetters")
        return firstLetters == secondLetters
    }
}
