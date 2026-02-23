class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        i = 0
        j = 0
        minlen = float('inf')
        begin = 0
        len1 = len(s1)
        len2 = len(s2)

        while i<len1:
            k = i

            while k<len1 and j<len2:
                if s1[k] == s2[j]:
                    j+=1
                k+=1
            
            if j<len2:
                break
            
            k -= 1
            end = k
            j = len2-1

            while k>=0 and j>=0:
                if s1[k] == s2[j]:
                    j-=1
                k-=1
            
            k+=1
            start = k
            j = 0

            if end-start+1<minlen:
                minlen = end-start+1
                begin = start
            
            i = start+1
        
        if minlen == float('inf'):
            return ""
        else:
            return s1[begin:begin+minlen]