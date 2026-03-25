from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visit = set()
        q.append(0)
        visit.add(0)

        while q:
            node = q.popleft()
            for val in rooms[node]:
                if val not in visit:
                    q.append(val)
                    visit.add(val)
        
        return len(visit) == len(rooms)
            

        