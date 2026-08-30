dirs = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
}

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x: int, y: int, current: str, seen: Set((int, int))):
            if len(current) == len(word):
                return word == current
        
            if not (0 <= y <= len(board) - 1):
                return
            if not (0 <= x <= len(board[0]) - 1):
                return
            if (x, y) in seen:
                return

            exploring = board[y][x]

            for diff_x, diff_y in dirs:
                seen.add((x, y))
                found = backtrack(x + diff_x, y + diff_y, current + exploring, seen)
                seen.remove((x,y))
                if found:
                    return True

            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if backtrack(x, y, "", set()):
                    return True

        return False