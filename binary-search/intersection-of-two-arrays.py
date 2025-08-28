class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        hasharray = [0] * 1001

        for nums in nums1:
            hasharray[nums] += 1
        
        for nums in nums2:
            if hasharray[nums] != 0:
                result.add(nums)
        
        return list(result)