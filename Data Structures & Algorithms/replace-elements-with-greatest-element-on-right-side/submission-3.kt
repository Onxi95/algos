import kotlin.math.max

class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        var maxOnRight = -1

        for (i in arr.indices.reversed()) {
            arr[i] = maxOnRight.also { maxOnRight = max(maxOnRight, arr[i]) }
        }

        return arr
    }
}
