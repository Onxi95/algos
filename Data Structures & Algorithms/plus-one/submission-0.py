class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for digit in digits[::-1]:
            current = digit + carry
            result.append(current % 10)
            carry = current // 10

        if carry:
            result.append(carry)

        return result[::-1]