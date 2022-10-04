##ss
class MyQueue:

    def __init__(self):
        
        self.q1 = []
        self.q2 = []
        self.ins = 0
        self.dels = 0

    def push(self, x: int) -> None:
        
        while len(self.q2)!=0:
            t = self.q2.pop()
            self.q1.append(t)
            
        self.q1.append(x)
        self.ins+=1

    def pop(self) -> int:
        
        while len(self.q1)!=0:
            t = self.q1.pop()
            self.q2.append(t)
            
        ans = self.q2.pop()
        self.dels-=1
        return ans

    def peek(self) -> int:
        if len(self.q1) == 0:
            return self.q2[-1]
        
        else:
            return self.q1[0]
        
        

    def empty(self) -> bool:
        #print(self.ins, self.dels)
        return abs(self.ins) == abs(self.dels)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
