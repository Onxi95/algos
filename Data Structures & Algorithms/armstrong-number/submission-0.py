class Solution:
    def isArmstrong(self, n: int) -> bool:
        copy = n
        length = 0
        while copy:
            copy = copy // 10
            length += 1

        total = 0
        copy = n
        while copy:
            digit = copy % 10
            copy = copy // 10
            total += digit ** length

        return total == n