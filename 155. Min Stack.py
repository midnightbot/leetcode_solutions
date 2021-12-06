class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val,self.mins[len(self.mins)-1]))
        

    def pop(self) -> None:
        self.stack.pop(len(self.stack)-1)
        self.mins.pop(len(self.mins)-1)
        
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
