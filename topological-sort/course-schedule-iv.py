from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        noden = defaultdict(list)
        nodein = [0] * numCourses
        ancest = [set() for _ in range(numCourses)]
        q = deque()

        for s, e in prerequisites:
            noden[s].append(e)
            nodein[e] +=1
        
        for i in range(len(nodein)):
            if nodein[i] == 0:
                q.append(i)
        
        while q:
            n = q.popleft()
            for nxt in noden[n]:
                ancest[nxt]|= ancest[n]
                ancest[nxt].add(n)

                nodein[nxt] -= 1
                if nodein[nxt] == 0:
                    q.append(nxt)

        res = []
        for s,e in queries:
            res.append(s in ancest[e])

        return res

        