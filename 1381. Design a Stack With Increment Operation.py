##ss
##Solution 1
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [-1 for x in range(maxSize)]
        self.index = 0
        self.size = maxSize

    def push(self, x: int) -> None:
        if self.index < self.size:
            self.stack[self.index] = x
            self.index+=1

    def pop(self) -> int:
        if self.index > 0:
            temp = self.stack[self.index-1]
            self.stack[self.index-1] = -1
            self.index-=1
            return temp
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if self.index > k:
            for x in range(k):
                self.stack[x]+=val
                
        elif self.index != 0 and self.index<=k:
            for x in range(self.index):
                self.stack[x]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

##Solution 2
##Almost same as Solution 1 just changes increment function
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [-1 for x in range(maxSize)]
        self.index = 0
        self.size = maxSize

    def push(self, x: int) -> None:
        if self.index < self.size:
            self.stack[self.index] = x
            self.index+=1

    def pop(self) -> int:
        if self.index > 0:
            temp = self.stack[self.index-1]
            self.stack[self.index-1] = -1
            self.index-=1
            return temp
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for x in range(min(self.index,k)):
            self.stack[x]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
