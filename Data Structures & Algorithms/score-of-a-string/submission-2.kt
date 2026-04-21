import kotlin.math.abs

class Solution {
    fun scoreOfString(s: String): Int {
        var result = 0
        for(i in 0 until s.length - 1) {
            val first = s[i]
            val second = s[i + 1]
            val diff = abs(first.code - second.code)
            result += diff
        }
        return result
    }
}
