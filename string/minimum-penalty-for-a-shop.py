class Solution:
    def bestClosingTime(self, customers: str) -> int:
        p = 0
        
        for c in customers:
            if c=='Y':
                p += 1
        
        besth = 0
        bestp = p
        n = len(customers)
        
        for i in range(n):
            if customers[i] == 'Y':
                p -= 1
            
            if customers[i] == 'N':
                p += 1
            
            if bestp > p:
                bestp = p
                besth = i+1
        
        return besth