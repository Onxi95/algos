class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        num = n
        new_num = 0
        while num:
            current = num % 10
            num = num // 10

            if current not in confusing:
                return False
            
            new_num = new_num * 10 + confusing[current]

        return new_num != n