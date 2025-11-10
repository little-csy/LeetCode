from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for index, val in enumerate(nums):
            while q and nums[q[-1]] < val:
                q.pop()
            q.append(index)

            if index - k >= q[0]:
                q.popleft()
            
            if index >= k-1:
                res.append(nums[q[0]])
        return res