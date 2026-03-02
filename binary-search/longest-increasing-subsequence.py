class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for x in nums:
            pos = len(tail)

            l = 0
            r = len(tail)-1

            while l<=r:
                mid = (l+r)//2
                if tail[mid] >= x:
                    pos = mid
                    r = mid -1
                else:
                    l = mid+1
            
            if pos == len(tail):
                tail.append(x)
            else:
                tail[pos] = x
        return len(tail)