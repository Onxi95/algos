class StringIterator:
    current_letter: str
    repeats: int
    rest: str

    def __init__(self, compressedString: str):
        (current_letter, repeats, rest) = self.parse_next_tokens(compressedString)

    def parse_next_tokens(self, s: str):
        letter = s[0]
        maybe_digit = ""
        rest_index = 1

        for possible_digit in s[1:]:
            if possible_digit.isnumeric():
                maybe_digit += possible_digit
                rest_index += 1
            else:
                break

        self.current_letter = letter
        self.repeats = int(maybe_digit)
        self.rest = s[rest_index:]
        return (letter, int(maybe_digit), s[rest_index:])
        

    def next(self) -> str:
        if self.repeats > 0:
            self.repeats -= 1
            return self.current_letter
        else:
            (_, _, rest) = self.parse_next_tokens(self.rest)
            if len(rest):
                return self.next()
            else:
                return " "

    def hasNext(self) -> bool:
        return True if len(self.rest) > 0 else False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
