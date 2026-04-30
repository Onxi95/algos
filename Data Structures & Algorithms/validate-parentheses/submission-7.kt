class Solution {
    fun isValid(s: String): Boolean {
        val stack = mutableListOf<Char>()
        val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')

        for (char in s) {
            if (char in pairs) {
                if(stack.isNotEmpty() && stack.last() == pairs[char]) {
                    stack.removeLast()
                } else {
                    return false
                }
            } else {
                stack.add(char)
            }
        }
        
        return stack.isEmpty()
    }
}
