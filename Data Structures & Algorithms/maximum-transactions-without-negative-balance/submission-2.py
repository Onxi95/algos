class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        current = 0
        min_heap = []

        for transaction in transactions:
            current += transaction
            heapq.heappush(min_heap, transaction)

            if current < 0:
                smallest = heapq.heappop(min_heap)
                current -= smallest
            
        return len(min_heap)