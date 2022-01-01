##ss
import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        
        self.blacklist = blacklist
        self.n = n
        #self.blacklist.append(float('inf'))
        if len(self.blacklist) >0 and self.n // len(self.blacklist) < 1000:
            self.vars = 1
            
            self.list = [x for x in range(self.n) if x not in self.blacklist]
            
        else:
            self.vars = 0
        

    def pick(self) -> int:
        
        if self.vars == 1:
            return random.choice(self.list)
            
        else:
            temp = randrange(self.n)
            if temp in self.blacklist:
                self.pick()
                
            return temp
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
