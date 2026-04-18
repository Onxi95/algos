class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if len(t) <= 0:
            return len(s)

        t_ptr = 0
        for letter in s:
            if t_ptr >= len(t):
                return len(t[t_ptr:])

            current_t = t[t_ptr]
            if current_t == letter:
                t_ptr += 1

        return len(t[t_ptr:])