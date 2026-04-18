class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        var result = IntArray(temperatures.size) { 0 }

        for (i in temperatures.indices) {
            var distance = 0
            for (j in i + 1 until temperatures.size) {
                val current = temperatures[i]
                val possible = temperatures[j]

                if (possible > current) {
                    result[i] = distance + 1
                    break
                } else {
                    distance++
                }
            }
        }

        return result
    }
}
