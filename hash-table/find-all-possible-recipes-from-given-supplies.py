from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}
        for r in recipes:
            indegree[r] = 0

        for reci,ingred in zip(recipes, ingredients):
            for i in ingred:
                graph[i].append(reci)
                indegree[reci] += 1
        
        q = deque()
        for supp in supplies:
            q.append(supp)
        
        res = []
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                indegree[nxt]-=1
                if indegree[nxt] == 0:
                    res.append(nxt)
                    q.append(nxt)
        return res
