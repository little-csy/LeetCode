class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0
        low = 0
        for w in s:
            if w == '(':
                low += 1
                high += 1
            elif w == ')':
                low -= 1
                high -=1
            else:
                high += 1
                low -= 1
            
            if high<0:
                return False
            low = max(0, low)
        
        return low == 0