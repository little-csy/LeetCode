class Allocator:

    def __init__(self, n: int):
        self.mem = [0]*n
        

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i] == 0:
                cnt+=1
            else:
                cnt = 0
            
            if cnt == size:
                start = i-size+1
                for j in range(start, start+size):
                    self.mem[j] = mID
                return start
        return -1

        

    def freeMemory(self, mID: int) -> int:
        num = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                num +=1
        return num

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)