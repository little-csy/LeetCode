class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            elif stack and s[i]!=stack[-1]:
                return False
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
