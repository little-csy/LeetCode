from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        ancestor = [set() for _ in range(numCourses)]
        q = deque()
        for s,e in prerequisites:
            graph[s].append(e)
            indegree[e]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                ancestor[nxt].add(node)
                ancestor[nxt] |= ancestor[node]

                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        res = []
        for s,e in queries:
            if s in ancestor[e]:
                res.append(True)
            else:
                res.append(False)
        return res