class Solution {
    fun lengthOfLastWord(s: String): Int {
        var ptr = s.length - 1
        while (ptr >= 0 && s[ptr] == ' ') {
            ptr -= 1
        }

        var result = 0
        while (ptr >= 0 && s[ptr] != ' ') {
            result += 1
            ptr -= 1
        }

        return result
    }
}
