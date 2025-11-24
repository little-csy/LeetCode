class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        # previous less (strict)
        prev = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next less or equal
        next_ = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            ans = (ans + arr[i] * left * right) % MOD

        return ans
