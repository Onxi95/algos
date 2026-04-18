class Solution {
    fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
        val sorted = position.zip(speed).sortedByDescending { it.first }
        val stack = mutableListOf<Double>()

        for ((position, speed) in sorted) {
            val timeAtEnd = (target - position).toDouble() / speed
            println("timeAtEnd: $timeAtEnd ($target - $position) / $speed")
            stack.add(timeAtEnd)
            if (stack.size >= 2 && stack.last() <= stack[stack.size - 2]) {
                stack.removeLast()
            }
        }

        return stack.size
    }
}
