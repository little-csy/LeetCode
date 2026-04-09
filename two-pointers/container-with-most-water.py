class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l<r:
            if height[l]<height[r]:
                h = height[l]
                w = r-l
                res = max(res, h*w)
                l+=1
            else:
                h = height[r]
                w = r-l
                res = max(res, h*w)
                r-=1
        return res