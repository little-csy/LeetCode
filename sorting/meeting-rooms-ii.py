import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []

        for s, e in intervals:
            if heap and s>heapq[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,e)
        return len(heapq)