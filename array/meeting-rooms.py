class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        stack = []
        for s,e in intervals:
            if not stack:
                stack.append(e)
                continue
            if s<stack[-1]:
                return False
        return True