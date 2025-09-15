import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        result = [0] * k
        prior_que = []

        for num in nums:
            map[num] += 1
        
        for key,value in map.items():
            heapq.heappush(prior_que, (value,key))
            if len(prior_que) > k:
                heapq.heappop(prior_que)
        
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(prior_que)[1]
        
        return result
