class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        possible_bills = [20, 10, 5]
        current_change = {bill: 0 for bill in possible_bills}

        for bill in bills:
            current_change[bill] += 1
            diff = bill - 5
            for possible_bill in possible_bills:
                while diff >= possible_bill and current_change[possible_bill]:
                    diff -= possible_bill
                    current_change[possible_bill] = current_change[possible_bill] - 1
            
            if diff > 0:
                return False

        return True
