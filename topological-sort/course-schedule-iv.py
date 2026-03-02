from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp = defaultdict(list)
        indegree = [0]*numCourses
        ancest = [set() for _ in range(numCourses)]
        q = deque()
        res = []

        for e, s in prerequisites:
            mp[s].append(e)
            indegree[e] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            for nxt in mp[node]:
                ancest[nxt].add(node)
                ancest[nxt] |= ancest[node]
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)
        
        for e, s in queries:
            if s in ancest[e]:
                res.append(True)
            else:
                res.append(False)
        
        return res

        