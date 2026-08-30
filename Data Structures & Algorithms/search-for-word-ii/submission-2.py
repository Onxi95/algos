class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        result = []

        directions = [
            # row | col
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for word in words:
            current = root
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = Trie()
                current = current.children[letter]
            current.end = True
            current.word = word


        def backtrack(row: int, col: int, seen: Set[(int, int)], current: Trie):
            if (row, col) in seen:
                return
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])):
                return

            curr_letter = board[row][col]
            if curr_letter not in current.children:
                return False

            curr_node = current.children[curr_letter]

            if curr_node.word is not None:
                result.append(curr_node.word)
                curr_node.word = None

            seen.add((row, col))
            for row_diff, col_diff in directions:
                backtrack(row + row_diff, col + col_diff, seen, curr_node)
            seen.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(row, col, set(), root)

        return result