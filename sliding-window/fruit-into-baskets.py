from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        hp = defaultdict(int)
        res = 0
        
        for r in range(len(fruits)):
            hp[fruits[r]] += 1
            while len(hp)>2 and l<len(fruits):
                hp[fruits[l]] -= 1
                if hp[fruits[l]] == 0:
                    del hp[fruits[l]]
                l+=1
            res = max(res, r-l+1)
        
        return res