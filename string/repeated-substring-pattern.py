class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = s+s
        cutss = ss[1:len(ss)-1]

        if cutss.find(s) == -1:
            return False
        else:
            return True