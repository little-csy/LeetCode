class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        stack = []
        for s,e in intervals:
            if not stack or s>=stack[-1][1]:
                stack.append([s,e])
            else:
                stack[-1][1] = max(stack[-1][1], e)
                
        if len(intervals) == len(stack):
            return True
        else:
            return False