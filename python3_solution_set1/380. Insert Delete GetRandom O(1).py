##ss
import random
class RandomizedSet:

    def __init__(self):
        self.dicts = {}
        self.que = []

    def insert(self, val: int) -> bool:
        if val not in self.dicts:
            self.dicts[val] = 1
            
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.dicts:
            self.dicts.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.dicts.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
