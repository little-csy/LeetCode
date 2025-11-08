import heapq
class MedianFinder:

    def __init__(self):
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.big, -num)

        if self.big and self.small and -self.big[0] > self.small[0]:
            heapq.heappush(self.small, -heapq.heappop(self.big))
        
        if len(self.big) > len(self.small)+1:
            heapq.heappush(self.small, -heapq.heappop(self.big))
        if len(self.small) > len(self.big)+1:
            heapq.heappush(self.big, heapq.heappop(self.small))
        

    def findMedian(self) -> float:
        if len(self.big) == len(self.small):
            return (-self.big[0] + self.small[0])/2
        elif len(self.big) > len(self.small):
            return -self.big[0]
        else:
            return self.small[0]

        
 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()