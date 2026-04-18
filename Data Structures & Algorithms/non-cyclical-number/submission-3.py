class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        num = str(n)

        while int(num) > 1:
            inner_total = 0
            for digit in num:
                inner_total += int(digit) ** 2
            if inner_total in seen:
                return False
            seen.add(inner_total)
            num = str(inner_total)

        return num == "1"