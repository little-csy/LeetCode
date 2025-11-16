class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        len1 = len(nums1)
        mid = len1//2
        if len1 % 2 == 1:
            return nums1[mid]
        if len1 % 2 == 0:
            return (nums1[mid]+nums1[mid-1])/2