##ss
from sortedcontainers import SortedList
##2 heaps approach
class SORTracker:

    def __init__(self):
        
        self.p = 0
        self.arr1 = SortedList()

    def add(self, name: str, score: int) -> None:
        
        self.arr1.add((-1*score,name))
        
        
        

    def get(self) -> str:
        
        self.p+=1
        #print(self.arr1.queue)
        return self.arr1[self.p-1][1]
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
