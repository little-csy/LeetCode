class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.deq = deque()
        self.result = []

        for i in range(len(nums)):
            self.winPop(nums[i])
            
            self.winPush(nums[i])

            if i >= k-1:
                self.winGetmax()
        
        return self.result
    
    def winPop(self, pop:int) -> None:
        if self.deq and pop == self.deq[0]:
            self.deq.popleft()

    def winPush(self, push:int) -> None:
        while self.deq and self.deq[-1] < push:
            self.deq.pop()
        
        self.deq.append(push)
        
    def winGetmax(self) -> None:
        self.result.append(self.deq[0])
        