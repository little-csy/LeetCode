class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i-1
                r = i+1

                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                
                while r<n-1 and arr[r+1]<arr[r]:
                    r+=1
                
                if r-l+1>res:
                    res = r-l+1
        return res
