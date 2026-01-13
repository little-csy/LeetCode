class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        presum = [1]*n
        postsum = [1]*n
        res = []
        presum[0] = nums[0]
        postsum[n-1] = nums[n-1]
        for i in range(1, n):
            presum[i] = presum[i-1]*nums[i]
        for j in range(n-2, -1, -1):
            postsum[j] = postsum[j+1]*nums[j]
        for k in range(n):
            if k>0 and k<n-1:
                res.append(presum[k-1]*postsum[k+1])
            elif k==0:
                res.append(1*postsum[k+1])
            elif k==n-1:
                res.append(1*presum[k-1])
        return res