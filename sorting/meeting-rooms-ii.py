import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = []
        for s, e in intervals:
            while heap and s>heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)