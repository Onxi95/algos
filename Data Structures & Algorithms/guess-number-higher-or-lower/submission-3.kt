/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *                1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num: Int): Int
 */

class Solution : GuessGame() {
    fun guessNumber(n: Int): Int {
        var left = 1
        var right = n
        while (left <= right) {
            val guess = left + (right - left) / 2
            when (guess(guess)) {
            0 -> return guess
            -1 -> right = guess - 1
            1 -> left = guess + 1
            }
        }
        return -1
    }
}
