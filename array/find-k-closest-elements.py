class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        tmp = []
        for i in range(len(arr)):
            dist = abs(arr[i]-x)
            tmp.append((dist, arr[i]))
        
        tmp.sort()

        for i in range(k):
            res.append(tmp[i][1])
        
        res.sort()
        
        return res