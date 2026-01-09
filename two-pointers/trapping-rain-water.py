class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1
        maxl = 0
        maxr = 0
        while left<=right:
            if height[left] <= height[right]:
                if height[left] >= maxl:
                    maxl = height[left]
                else:
                    res += maxl - height[left]
                left += 1
            else:
                if height[right] >= maxr:
                    maxr = height[right]
                else:
                    res += maxr - height[right]
                right -= 1
        
        return res