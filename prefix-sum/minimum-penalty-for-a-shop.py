class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minp = float('inf')
        minh = -1
        n = len(customers)
        for t in range(n+1):
            p = 0
            for i in range(t):
                if customers[i] == 'N':
                    p+=1
            
            for j in range(t,n):
                if customers[j] == 'Y':
                    p+=1
            if p<minp:
                minp = p
                minh=t
        return minh