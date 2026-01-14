class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == stack[-1]:
                stack.pop()
            elif len(stack) == 0 or s[i] != stack[-1]:
                return False
            else:
                stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
        