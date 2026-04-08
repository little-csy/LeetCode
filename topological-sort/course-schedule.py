from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()
        cnt = 0

        for e,s in prerequisites:
            graph[s].append(e)
            indegree[e]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            cnt += 1
            for nxt in graph[node]:
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if cnt == numCourses:
            return True
        else:
            return False