from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp = defaultdict(list)
        indegree = [0] * numCourses
        ancest = [set() for _ in range(numCourses)]
        q = deque()

        for s,e in prerequisites:
            mp[s].append(e)
            indegree[e]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            for val in mp[node]:
                ancest[val].add(node)
                ancest[val] |= ancest[node]
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        
        res = []
        for s,e in queries:
            if s in ancest[e]:
                res.append(True)
            else:
                res.append(False)
        return res