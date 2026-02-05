class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        len1 = len(s1)
        len2 = len(s2)
        i = 0
        minlen = float("inf")
        begin = 0

        while i < len1:
            j = 0
            k = i

            while k<len1 and j<len2:
                if s1[k] == s2[j]:
                    j+=1
                k+=1
            
            if j<len2:
                break
            
            end = k-1
            j = len2-1
            k-=1

            while j>=0 and k>=0:
                if s1[k] == s2[j]:
                    j-=1
                k-=1
            
            start = k+1

            if end-start+1 < minlen:
                minlen = end-start+1
                begin = start
            
            i = start+1
        if minlen == float("inf"):
            return ""
        else:
            return s1[begin:begin+minlen]