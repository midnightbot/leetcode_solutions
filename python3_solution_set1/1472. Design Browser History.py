##ss
class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = []
        self.arr.append(homepage)
        self.pointer = 0
        

    def visit(self, url: str) -> None:
        self.pointer+=1
        self.arr = self.arr[0:self.pointer]
        self.arr.append(url)
        

    def back(self, steps: int) -> str:
        
        self.pointer = max(0,self.pointer - steps)
        return self.arr[self.pointer]
        

    def forward(self, steps: int) -> str:
        self.pointer = min(len(self.arr)-1,self.pointer+steps)
        
        return self.arr[self.pointer]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
