class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        val stack = ArrayDeque<String>()
        for (token in tokens) {
            if (token in "+-*/") {
                if (stack.size < 2) {
                    return 0
                }
                val first = stack.removeLast().toInt()
                val second = stack.removeLast().toInt()
                val result = when (token) {
                    "+" -> first + second
                    "-" -> second - first
                    "*" -> first * second
                    "/" -> second / first
                    else -> throw IllegalArgumentException("invalid operator: $token")
                }
                stack.addLast(result.toString())
            } else {
                stack.addLast(token)
            }
        }
        return if (stack.size == 1) stack.last().toInt() else 0
    }
}
