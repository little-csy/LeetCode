class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = {
            "0":"",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            }
        res = []
        path = []

        def backtrack(digits, start):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for val in s[digits[start]]:
                path.append(val)
                backtrack(digits, start+1)
                path.pop()
        
        backtrack(digits, 0)
        return res