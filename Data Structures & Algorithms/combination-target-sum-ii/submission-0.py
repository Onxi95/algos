class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index: int, current: List[int], total: int):
            if total == target:
                result.append(current[:])
                return
            if index >= len(candidates) or total > target:
                return

            current.append(candidates[index])
            backtrack(index + 1, current, total + candidates[index])
            current.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)

        return result