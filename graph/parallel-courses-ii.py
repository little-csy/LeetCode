from collections import deque
from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre = [0] * n
        for prv, nxt in relations:
            pre[nxt-1] |= 1<<(prv-1)
        q =deque()
        visit = set()
        q.append((0, 0))
        visit.add(0)

        while q:
            mask, step = q.popleft()

            if mask == (1<<n)-1:
                return step

            can = []
            for i in range(n):
                if (mask & (1<<i))==0 and pre[i] == (pre[i] & mask):
                    can.append(i)
            
            if len(can)<=k:
                newmask = mask
                for c in can:
                    newmask |= (1<<c)
                if newmask not in visit:
                    visit.add(newmask)
                    q.append((newmask, step+1))
            else:
                for comb in combinations(can, k):
                    newmask = mask
                    for c in comb:
                        newmask |= (1<<c)
                    if newmask not in visit:
                        visit.add(newmask)
                        q.append((newmask, step+1))
        return -1