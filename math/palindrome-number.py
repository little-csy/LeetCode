class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        if s == list(reversed(s)):
            return True
        else:
            return False