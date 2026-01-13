class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float("-inf")]*(len(nums1)+1) for _ in range(len(nums2)+1)]

        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                dp[i][j] = max(dp[i-1][j-1]+nums2[i-1]*nums1[j-1], nums2[i-1]*nums1[j-1], dp[i-1][j], dp[i][j-1])
        
        return dp[i][j]