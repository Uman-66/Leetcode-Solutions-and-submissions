class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()    
        result = []
        combo = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                result.append(combo[:])   
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                combo.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])   
                combo.pop() 
        backtrack(0, target)
        return result