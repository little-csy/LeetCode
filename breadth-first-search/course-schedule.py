from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node = defaultdict(list)
        nodein = [0] * numCourses
        nums = []
        for nxt, pre in prerequisites:
            node[pre].append(nxt)
            nodein[nxt] += 1
        
        q = deque()
        for i in range(numCourses):
            if nodein[i] == 0:
                q.append(i)
        
        while q:
            n = q.popleft()
            nums.append(n)
            for val in node[n]:
                nodein[val]  -= 1
                if nodein[val] == 0:
                    q.append(val)
        
        if len(nums) == numCourses:
            return True
        else:
            return False