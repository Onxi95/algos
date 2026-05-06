class Solution {
    fun hammingWeight(n: Int): Int {
        var total = 0
        var number = n
        while (number > 0) {
            val current = number and 1
            if(current == 1) {
                total++
            }
            number = number shr 1
        }

        return total
    }
}
