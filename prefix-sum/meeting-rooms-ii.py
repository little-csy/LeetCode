class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        event = []
        for start,end in intervals:
            event.append((start, +1))
            event.append((end, -1))

        event.sort(key = lambda x: (x[0],x[1]))

        cur = 0
        best = 0

        for i in range(len(event)):
            cur+=event[i][1]
            if cur>best:
                best = cur
        
        return best
