from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()
        res = []

        for e, s in prerequisites:
            mp[s].append(e)
            indegree[e]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)

            for nxt in mp[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if len(res) == numCourses:
            return True
        else:
            return False
