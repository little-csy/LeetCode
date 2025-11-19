from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (A,B), val in zip(equations,values):
            graph[A][B] = val
            graph[B][A] = 1/val
        
        def dfs(start,end,visit):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visit.add(start)

            for nei, val in graph[start].items():
                if nei not in visit:
                    tmp = dfs(nei,end,visit)
                    if tmp!=-1.0:
                        return tmp*val
            return -1.0
        
        res = []
        for c,d in queries:
            res.append(dfs(c,d,set()))
        return res