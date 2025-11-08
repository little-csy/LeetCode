class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                temp.reverse()
                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                if num:
                    rep = int(''.join(num))
                else:
                    rep = 1
                
                new = rep * (''.join(temp))
                stack.append(new)
        
        return ''.join(stack)