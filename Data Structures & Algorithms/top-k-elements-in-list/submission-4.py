class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            arr[cnt].append(num)

        result = []
        for i in range(len(arr) -1, 0, -1):
            if arr[i]:
                for num in arr[i]:
                    result.append(num)
            if len(result) == k:
                return result

        return result