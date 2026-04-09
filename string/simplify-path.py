class Solution:
    def simplifyPath(self, path: str) -> str:
        part = path.split('/')
        stack = []
        for p in part:
            if p == '' or p=='.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)