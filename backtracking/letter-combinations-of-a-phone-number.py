class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
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

        def dfs(digits, start):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            
            for val in s[digits[start]]:
                path.append(val)
                dfs(digits, start+1)
                path.pop()
        
        dfs(digits, 0)
        
        return res