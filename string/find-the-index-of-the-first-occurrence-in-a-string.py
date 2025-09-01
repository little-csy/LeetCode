class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        if nlen == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+nlen] == needle:
                return i
        return -1