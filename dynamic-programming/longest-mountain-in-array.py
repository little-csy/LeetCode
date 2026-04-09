class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        length = 0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                l = i-1
                r = i+1
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                if r-l+1>length:
                    length = r-l+1
        return length
                