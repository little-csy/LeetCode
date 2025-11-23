class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        color = [0] * n
        res = []
        cnt = 0

        for i,c in queries:
            if color[i] != 0:
                if i>0 and color[i]==color[i-1]:
                    cnt-=1
                if i<n-1 and color[i] == color[i+1]:
                    cnt-=1
            
            color[i] = c

            if i>0 and color[i]==color[i-1]:
                cnt+=1
            if i<n-1 and color[i] == color[i+1]:
                cnt+=1
            
            res.append(cnt)

        return res