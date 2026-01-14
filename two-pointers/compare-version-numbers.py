class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        n = max(len(v1), len(v2))

        for i in range(n):
            if i < len(v1):
                a = int(v1[i])
            else:
                a = 0
            
            if i < len(v2):
                b = int(v2[i])
            else:
                b = 0

            if a<b:
                return -1
            if a>b:
                return 1
        return 0