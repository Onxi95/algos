class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        real_sizes = []
        current_max = float('inf')
        for size in warehouse:
            current = min(current_max, size)
            current_max = current
            real_sizes.append(current)
        
        boxes.sort()

        right = len(real_sizes) - 1
        left = 0

        total = 0

        while left < len(boxes) and right >= 0:
            if boxes[left] <= real_sizes[right]:
                left += 1
                right -= 1
                total += 1
            else:
                right -= 1

        return total