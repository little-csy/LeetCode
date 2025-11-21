class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        event = []
        for p, r in lights:
            event.append((p-r, +1))
            event.append((p+r+1, -1))
        
        event.sort()

        cur = 0
        maxl = 0
        res = 0

        for place, val in event:
            cur += val
            if cur>maxl:
                maxl = cur
                res = place
        return res
