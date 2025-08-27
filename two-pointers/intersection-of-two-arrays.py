class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1 = set(nums1)
        h2 = set(nums2)
        return list(h1&h2)