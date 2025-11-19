class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        def apply():
            a = nums.pop()
            b= nums.pop()
            o = ops.pop()
            if o =='+':
                nums.append(a+b)
            else:
                nums.append(b-a)
        
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
