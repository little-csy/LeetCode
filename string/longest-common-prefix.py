class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s)==i or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]
