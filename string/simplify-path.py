class Solution:
    def simplifyPath(self, path: str) -> str:
        part = path.split('/')
        stack = []
        for w in part:
            if w == '.' or w == '':
                continue
            elif w == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(w)
        return '/' + '/'.join(stack)