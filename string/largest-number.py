from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str,nums))

        def cmp(a,b):
            if a+b>b+a:
                return -1
            elif b+a>a+b:
                return 1
            else:
                return 0
        
        s.sort(key=cmp_to_key(cmp))

        if s[0]=='0':
            return "0"
        
        return ''.join(s)
        