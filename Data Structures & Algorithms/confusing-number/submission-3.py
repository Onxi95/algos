class Solution:
    def confusingNumber(self, n: int) -> bool:
        weird_num = 0
        i = 0

        invalid = [2,3,4,5,7]
        valid_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        n_copy = n
        while n_copy > 0:
            right_digit = n_copy % 10
            if right_digit in invalid:
                return False
            
            weird_num = weird_num * 10 + valid_map[right_digit]
            i += 1
            n_copy //= 10
            
        return weird_num != n