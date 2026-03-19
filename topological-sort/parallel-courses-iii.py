from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n+1)
        q = deque()
        dp = [0] * (n+1)

        for pre, nxt in relations:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i-1]
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                dp[nei] = max(dp[nei], dp[node]+time[nei-1])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return max(dp)