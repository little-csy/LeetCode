class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights = [0] + heights
        heights.append(0)
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                mid = stack.pop()
                r = stack[-1]
                l = i
                w = l-r-1
                h = heights[mid]
                res = max(res, h*w)
            
            stack.append(i)
        
        return res