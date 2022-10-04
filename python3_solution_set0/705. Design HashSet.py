##ss
class MyHashSet:

    def __init__(self):
        self.dicts = {}
        

    def add(self, key: int) -> None:
        self.dicts[key] = 1
        
        

    def remove(self, key: int) -> None:
        if key in self.dicts:
            self.dicts.pop(key)
        

    def contains(self, key: int) -> bool:
        return key in self.dicts
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
