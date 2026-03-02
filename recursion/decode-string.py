class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                tmp = []
                while stack and stack[-1]!='[':
                    tmp.append(stack.pop())
                tmp.reverse()
                tmp = ''.join(tmp)
                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                if num:
                    num = int(''.join(num))
                else:
                    num = 1
                
                new = num*(tmp)
                stack.append(new)
        
        return ''.join(stack)