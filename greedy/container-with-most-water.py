class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1
        while left<=right:
            w = right-left
            h = min(height[right],height[left])
            res = max(res, w*h)
            if height[right] <= height[left]:
                right-=1
            else:
                left+=1
        return res