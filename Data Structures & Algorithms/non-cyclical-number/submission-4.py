class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.decompose(n)

        return True if n == 1 else False
    
    def decompose(self, n: int) -> int:
        total = 0
        while n:
            reminder = n % 10
            total += reminder**2
            n = n // 10

        return total
