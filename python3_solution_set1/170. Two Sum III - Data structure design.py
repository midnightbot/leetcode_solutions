##ss
class TwoSum:

    def __init__(self):
        
        self.dicts = {}
        

    def add(self, num: int) -> None:
        
        self.dicts[num] = self.dicts.get(num,0) + 1
        

    def find(self, value: int) -> bool:
        
        for x in self.dicts:
            if value - x in self.dicts:
                if value - x == x and self.dicts[x] >=2:
                    return True
                
                elif value-x !=x:
                    return True
            
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
