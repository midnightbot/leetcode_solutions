from collections import deque
class FirstUnique:
    

    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.unique = {}
        for x in nums:
            self.add(x)
        
        

    def showFirstUnique(self) -> int:
        while self.queue and not self.unique[self.queue[0]]:
            self.queue.popleft()
            
        if self.queue:
            return self.queue[0]
        
        return -1
        
        
        

    def add(self, value: int) -> None:
        if value not in self.unique:
            self.unique[value] = True
            self.queue.append(value)
            
        else:
            self.unique[value] = False
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
