class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        sortp = [False] * (n-1)
        ans = 0

        for c in range(m):
            bad = False

            for r in range(n-1):
                if not sortp[r] and strs[r][c]> strs[r+1][c]:
                    bad = True
                    break
                
            if bad == True:
                ans+=1
                continue
            
            for r in range(n-1):
                if not sortp[r] and strs[r][c]< strs[r+1][c]:
                    sortp[r] = True
        return ans 