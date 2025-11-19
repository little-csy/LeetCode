from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}

        for person in range(1,n+1):
            if person not in color:
                q = deque([person])
                color[person] = 0
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            color[nei] = 1-color[node]
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True