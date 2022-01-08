##ss
import random
class RandomizedCollection:

    def __init__(self):
        self.dicts = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dicts:
            self.dicts[val]+=1
            self.list.append(val)
            return False
        else:
            self.dicts[val] = 1
            self.list.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.dicts:
            self.dicts[val]-=1
            self.list.remove(val)
            if self.dicts[val] == 0:
                self.dicts.pop(val)
                
                
            return True
        
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
