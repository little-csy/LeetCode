class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, x in enumerate(height):
            while stack and height[stack[-1]] < x:
                mid = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]])
                    w = i - stack[-1] - 1
                    res += (h-height[mid])*w
            
            stack.append(i)
        
        return res
