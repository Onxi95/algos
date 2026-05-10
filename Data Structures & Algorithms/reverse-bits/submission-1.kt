class Solution {
    fun reverseBits(n: Int): Int {
        var result = 0
        for (i in 0 until 32) {
            val current = (n shr i) and 1
            result = result or (current shl (31 - i))
        }
        return result
    }
}
