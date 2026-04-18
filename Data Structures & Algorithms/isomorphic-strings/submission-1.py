class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t_map = {}
        t_s_map = {}

        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]

            if not letter_s in s_t_map:
                s_t_map[letter_s] = letter_t
            if not letter_t in t_s_map:
                t_s_map[letter_t] = letter_s
            
            assoc_s = s_t_map[letter_s]
            assoc_t = t_s_map[letter_t]
            if assoc_s != letter_t or assoc_t != letter_s:
                return False

        return True