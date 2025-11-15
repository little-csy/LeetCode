class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(candidates, target, sums, start, used):
            if sums > target:
                return
            if sums == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i>0 and candidates[i] == candidates[i-1] and used[i-1] == 0:
                    continue
                path.append(candidates[i])
                sums += candidates[i]
                used[i] = 1
                backtracking(candidates, target, sums, i+1, used)
                sums -= candidates[i]
                used[i] = 0
                path.pop()
        
        used = [0] * len(candidates)
        candidates.sort()
        backtracking(candidates, target, 0, 0, used)

        return res