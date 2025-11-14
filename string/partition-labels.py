class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = {}
        res = []
        left = 0
        right = 0
        for index, val in enumerate(s):
            hash[val] = index
        
        for i in range(len(s)):
            right = max(right, hash[s[i]])
            if i == right:
                res.append(right-left+1)
                left = i+1
        return res
