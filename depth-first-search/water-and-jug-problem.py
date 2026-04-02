from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        if target>x+y:
            return False
        q = deque()
        visit = set()
        q.append((0,0))
        visit.add((0,0))
        while q:
            a, b = q.popleft()
            if a+b==target:
                return True
            nextStatus = []
            #fillx
            nextStatus.append((x,b))
            #filly
            nextStatus.append((a,y))
            #emptyx
            nextStatus.append((0,b))
            #emptyy
            nextStatus.append((a,0))
            #x->y
            pour = min(a,y-b)
            nextStatus.append((a-pour,b+pour))
            #y->x
            pour = min(x-a,b)
            nextStatus.append((a+pour,b-pour))

            for nxt in nextStatus:
                if nxt not in visit:
                    q.append(nxt)
                    visit.add(nxt)
        return False