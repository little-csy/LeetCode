class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        e = 1e-6
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0]-24) < e
            
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    a = nums[i]
                    b = nums[j]

                    rest = []
                    for k in range(len(nums)):
                        if k!=i and k!=j:
                            rest.append(nums[k])
                    
                    candidate = [
                        a+b,
                        a-b,
                        b-a,
                        a*b,
                    ]

                    if abs(b)>e:
                        candidate.append(a/b)
                    if abs(a)>e:
                        candidate.append(b/a)
                    
                    for val in candidate:
                        if dfs(rest+[val]):
                            return True
            return False

        start = []
        for x in cards:
            start.append(float(x))
        
        return dfs(start)