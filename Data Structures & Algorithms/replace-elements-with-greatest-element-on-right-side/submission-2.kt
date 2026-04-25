import kotlin.math.max

class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        if (arr.isEmpty()) {
            return intArrayOf()
        }
        var maxOnRight = arr.last()
        for (i in arr.size - 2 downTo 0) {
            val snapshot = arr[i]
            arr[i] = maxOnRight
            maxOnRight = max(snapshot, maxOnRight)
        }
        arr[arr.size - 1] = -1

        return arr
    }
}
