class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val rows = Array(9) { mutableSetOf<Char>() }
        val cols = Array(9) { mutableSetOf<Char>() }
        val squares = Array(9) { mutableSetOf<Char>() }

        for (row in 0 until 9) {
            for (col in 0 until 9) {
                val squareHash = (row / 3) * 3 + (col / 3)
                val current = board[row][col]

                if (current == '.') continue
                if (current in rows[row] || current in cols[col] || current in squares[squareHash]) {
                    return false
                }

                rows[row].add(current)
                cols[col].add(current)
                squares[squareHash].add(current)
            }
        }

        return true;
    }
}
