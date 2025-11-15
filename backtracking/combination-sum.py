class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        def backtracking(candidates, target, sums, start):
            if sums > target:
                return
            if sums == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                sums += candidates[i]
                backtracking(candidates, target, sums, i)
                sums -= candidates[i]
                path.pop()
        
        backtracking(candidates, target, 0, 0)
        return res
                