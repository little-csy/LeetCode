class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")

        def helper(i):
            sign = '+'
            num = 0
            stack = []
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num*10 + int(c)
                
                if c == '(':
                    num, i = helper(i + 1)
            
                if (not c.isdigit() and c != '(') or i==len(s)-1:
                    if sign=='+':
                        stack.append(num)
                    elif sign=='-':
                        stack.append(-num)
                    elif sign=='*':
                        stack[-1] = stack[-1]*num
                    elif sign=='/':
                        stack[-1] = int(stack[-1]/num)
                
                    sign = c
                    num = 0
                
                if c == ')':
                    return sum(stack), i
                i += 1
            
            return sum(stack), i
        
        result, _ = helper(0)
        return result