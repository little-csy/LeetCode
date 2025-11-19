class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        def prev_char(i):
            j = i - 1
            while j >= 0 and s[j] == ' ':
                j -= 1
            return s[j] if j >= 0 else None
        def apply():
            b = nums.pop()
            a = nums.pop()
            o = ops.pop()
            if o =='+':
                nums.append(a+b)
            else:
                nums.append(a-b)
        
        i = 0
        n = len(s)

        while i<n:
            c = s[i]
            if c==' ':
                i+=1
            elif c.isdigit():
                num = 0
                while i<n and s[i].isdigit():
                    num = 10*num + int(s[i])
                    i+=1
                nums.append(num)
            elif c=='+' or c=='-':
                p = prev_char(i)
                if c == '-' and (p is None or p in "(+-"):
                    nums.append(0)
                while ops and ops[-1] in '+-':
                    apply()
                ops.append(c)
                i+=1
            elif c=='(':
                ops.append(c)
                i+=1
            elif c==')':
                while ops and ops[-1]!='(':
                    apply()
                ops.pop()
                i+=1
        while ops:
            apply()
        return nums[-1]
