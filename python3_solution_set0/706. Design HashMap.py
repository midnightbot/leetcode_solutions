##ss
class MyHashMap:

    def __init__(self):
        self.dicts = {}
        

    def put(self, key: int, value: int) -> None:
        
        self.dicts[key] = value
        

    def get(self, key: int) -> int:
        if key in self.dicts.keys():
            return self.dicts[key]
        
        else:
            return -1
        

    def remove(self, key: int) -> None:
        self.dicts.pop(key,None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
