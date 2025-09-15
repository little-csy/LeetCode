class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        result = []

        for num in nums:
            map[num] += 1
        
        sorted_items = sorted(map.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            result.append(sorted_items[i][0])
    
        return result
        