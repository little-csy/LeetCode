class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        stack = []

        for c in p:
            if c=='.' or c=='':
                continue
            elif c=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/'+'/'.join(stack)
                    