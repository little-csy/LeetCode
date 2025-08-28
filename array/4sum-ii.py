class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = defaultdict(int)
        cnt = 0
        for value1 in nums1:
            for value2 in nums2:
                hashmap[value1+value2] += 1
        
        for value3 in nums3:
            for value4 in nums4:
                target = 0 - (value3+value4)
                if target in hashmap:
                    cnt += hashmap[target]
        
        return cnt