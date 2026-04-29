class Solution {
    fun isPalindrome(s: String): Boolean {
        var left = 0
        var right = s.length - 1
        
        while (left < right) {
            while (!s[left].isLetterOrDigit() && left < right) {
                left++
            }
            while (!s[right].isLetterOrDigit() && left < right) {
                right--
            }
            
            if (s[left].lowercase() != s[right].lowercase()) {
                return false
            }
            
            left++
            right--
        }

        return true
    }
}
