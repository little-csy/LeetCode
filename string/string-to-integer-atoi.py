class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i<n and s[i] == ' ':
            i+=1
        
        sig = 1
        if i<n and s[i]=='+':
            sig = 1
            i+=1
        elif i<n and s[i]=='-':
            sig = -1
            i+=1
        
        num = 0
        INTMAX = 2**31-1
        INTMIN = -2**31
        while i<n and s[i].isdigit():
            digit = ord(s[i])-ord('0')
            if num>INTMAX//10 or (num == INTMAX//10 and digit>INTMAX%10):
                if sig==1:
                    return INTMAX
                else:
                    return INTMIN
            num = num*10 + digit
            i+=1
        
        return sig*num