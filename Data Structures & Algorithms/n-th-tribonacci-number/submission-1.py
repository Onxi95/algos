class Solution:
    def __init__(self):
        self.memory = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        n1 = self.memory[n - 1] if (n - 1) in self.memory else self.tribonacci(n - 1)
        n2 = self.memory[n - 2] if (n - 2) in self.memory else self.tribonacci(n - 2)
        n3 = self.memory[n - 3] if (n - 3) in self.memory else self.tribonacci(n - 3)
        self.memory[n - 1] = n1
        self.memory[n - 2] = n2
        self.memory[n - 3] = n3
        return n1 + n2 + n3