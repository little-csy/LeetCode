class MyStack:

    def __init__(self):
        self.queue_in=deque()
        self.queue_out=deque()
        
    def push(self, x: int) -> None:
        self.queue_in.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.queue_in)-1):
            self.queue_out=self.queue_in.popleft()
        
        self.queue_out, self.queue_in = self.queue_in, self.queue_out
        return self.queue_out.popleft()

    def top(self) -> int:
        return self.queue_in[-1]
        
    def empty(self) -> bool:
        if self.queue_in is None:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()