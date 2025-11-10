class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) -1
        maxL = 0
        maxR = 0
        while left<right:
            if height[left] < height[right]:
                if height[left] < maxL:
                    res += maxL - height[left]
                else:
                    maxL = height[left]
                left += 1
            else:
                if height[right] < maxR:
                    res += maxR - height[right]
                else:
                    maxR = height[right]
                right -= 1

        return res