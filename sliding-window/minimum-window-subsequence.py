class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        lens1 = len(s1)
        lens2 = len(s2)
        i = 0
        j = 0
        begin = 0
        minlen = float('inf')

        while i<lens1:
            k = i

            while k<lens1 and j<lens2:
                if s1[k] == s2[j]:
                    j+=1
                k+=1
            
            if j<lens2:
                break
            
            end = k-1
            k -= 1
            j = lens2-1

            while k>=0 and j>=0:
                if s1[k] == s2[j]:
                    j-=1
                k-=1
            
            start = k+1
            k += 1
            j = 0

            if end-start+1<minlen:
                minlen = end-start+1
                begin = start
            
            i = start+1
        
        if minlen == float('inf'):
            return ""
        else:
            return s1[begin:begin+minlen]