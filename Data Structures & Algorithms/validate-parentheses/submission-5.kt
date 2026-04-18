import java.util.Stack

class Solution {
    fun isValid(s: String): Boolean {
        var stack = Stack<Char>()
        val pairs = mapOf<Char, Char>(
            ')' to '(',
            ']' to '[',
            '}' to '{'
        )

        for (parenthese in s) {
            if (parenthese in pairs.values) {
                stack.add(parenthese)
            } else {
                if (stack.isEmpty()) {
                    return false
                }
                val lastFromStack = stack.pop()
                val toCompare = pairs[parenthese]
                if (lastFromStack != toCompare) {
                    return false
                }

            }
        }

        return stack.size == 0
    }
}
