from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        heap = []
        res = []

        for val, freq in n.items():
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for freq, val in heap:
            res.append(val)
        
        return res