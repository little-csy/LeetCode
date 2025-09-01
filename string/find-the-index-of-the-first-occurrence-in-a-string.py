class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j>0 and haystack[i] != needle[j]:
                j = next[j-1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                return i - j + 1
        
        return -1

    def getNext(self, next:List[int], needle:str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(next)):
            while j>0 and needle[i] != needle[j]:
                j = next[j-1]
                
            if needle[i] == needle[j]:
                j += 1

            next[i] = j


