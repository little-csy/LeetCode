class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        if x <0 or (x % 10 == 0 and x!=0):
            return False

        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        
        if x == rev or x == rev // 10:
            return True
        else:
            return False