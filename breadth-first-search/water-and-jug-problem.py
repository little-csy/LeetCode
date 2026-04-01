from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        if target>x+y:
            return False
        
        q = deque()
        q.append((0,0))
        visit = set()
        visit.add((0,0))

        while q:
            a, b = q.popleft()
            if a==target or b==target or a+b==target:
                return True
            nextStatus = []

            #fill x
            nextStatus.append((x,b))
            #fill y
            nextStatus.append((a,y))
            #empty x
            nextStatus.append((0,b))
            #empty y
            nextStatus.append((a,0))
            #x->y
            pourx = min(a, y-b)
            nextStatus.append((a-pourx,b+pourx))
            #y->x
            poury = min(x-a,b)
            nextStatus.append((a+poury,b-poury))

            for nxt in nextStatus:
                if nxt not in visit:
                    q.append(nxt)
                    visit.add(nxt)
        
        return False