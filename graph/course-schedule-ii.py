from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        indegree = [0] * numCourses
        num = []
        q = deque()

        for e, s in prerequisites:
            mp[s].append(e)
            indegree[e]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            num.append(node)

            for val in mp[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        
        if len(num) == numCourses:
            return num
        else:
            return []