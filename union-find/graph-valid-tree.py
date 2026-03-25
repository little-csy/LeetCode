from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
            
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque()
        visit = set()
        q.append(0)
        visit.add(0)

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        
        return len(visit) == n

        