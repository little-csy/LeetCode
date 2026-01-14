class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = 0
        cnt = 0
        for x in nums:
            if cnt == 0:
                cand = x
                cnt+=1
            else:
                if x==cand:
                    cnt+=1
                else:
                    cnt-=1
        
        return cand