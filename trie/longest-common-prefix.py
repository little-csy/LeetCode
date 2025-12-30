class Solution:
    def longestCommonPrefix(self, strs):
        res = []
        for char in zip(*strs):
            if len(set(char)) == 1:
                res.append(char[0])
            else:
                break
        return ''.join(res)