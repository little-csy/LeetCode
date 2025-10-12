class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
        return res