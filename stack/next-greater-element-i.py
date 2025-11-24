class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            i = nums2.index(num1)
            found = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>num1:
                    found = nums2[j]
                    break
            res.append(found)
        return res