from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        visit = set()
        stack = []

        for c in s:
            counter[c]-=1
            if c in visit:
                continue
            while stack and stack[-1]>c and counter[stack[-1]]:
                val = stack.pop()
                visit.remove(val)
            stack.append(c)
            visit.add(c)
        
        return "".join(stack)
