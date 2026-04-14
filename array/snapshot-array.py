import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snapid = 0
        self.history = [[(0,0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        arr = self.history[index]
        if arr[-1][0]==self.snapid:
            arr[-1] = (self.snapid,val)
        else:
            arr.append((self.snapid,val))
        
    def snap(self) -> int:
        self.snapid += 1
        return self.snapid-1
        
    def get(self, index: int, snap_id: int) -> int:
        arr = self.history[index]
        post = bisect.bisect_right(arr, (snap_id,float('inf')))
        return arr[post-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)