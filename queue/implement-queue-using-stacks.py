class MyQueue:

    def __init__(self):
        self.stackin=[]
        self.stackout=[]
        
    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:

        if self.stackout:
            return self.stackout.pop()
        
        else:
            for i in range(len(self.stackin)):
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()
        

    def peek(self) -> int:
        top = self.pop()
        self.stackout.append(top)
        return top
        

    def empty(self) -> bool:
        if self.stackin or self.stackout:
            return False
        else:
            return True
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()