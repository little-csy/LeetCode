from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        ind = [0]*numCourses
        for e,s in prerequisites:
            mp[s].append(e)
            ind[e]+=1
        
        q = deque()
        
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            node = q.popleft()
            cnt+=1
            
            for v in mp[node]:
                ind[v]-=1
                if ind[v] == 0:
                    q.append(v)
        
        return cnt == numCourses