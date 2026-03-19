from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n+1)
        q = deque()
        taken = 0
        semester = 0

        for pre,nxt in relations:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                taken += 1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            semester += 1
        
        if taken == n:
            return semester
        else:
            return -1