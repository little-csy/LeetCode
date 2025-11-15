class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(k, n, sum, start):
            if len(path) == k:
                if sum == n:
                    res.append(path[:])
                return
            for i in range(start, 10):
                sum += i
                path.append(i)
                backtrack(k, n, sum, i+1)
                sum -=i
                path.pop()
        
        backtrack(k, n, 0, 1)
        return res
        