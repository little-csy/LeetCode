class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasharray = [0] * 26
        for i in range(len(s)):
            hasharray[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            hasharray[ord(t[i])-ord('a')] -= 1
        for i in range(26):
            if hasharray[i] !=0:
                return False
        return True