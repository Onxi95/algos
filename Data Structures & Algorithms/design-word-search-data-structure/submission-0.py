class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(index: int, root: Optional[Node]) -> bool:
            if not root:
                return False

            current = root
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for c in current.children.values():
                        if dfs(i + 1, c):
                            return True
                if char in current.children:
                    current = current.children[char]
                else:
                    return False

            return current.is_end
        
        return dfs(0,self.root)