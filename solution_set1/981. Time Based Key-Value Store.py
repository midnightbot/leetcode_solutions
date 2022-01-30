##ss
from queue import PriorityQueue
class TimeMap:

    def __init__(self):
        self.dicts = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dicts:
            self.dicts[key].put((timestamp,value))
        else:
            self.dicts[key] = PriorityQueue()
            self.dicts[key].put((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.dicts:
            #return self.dicts[key].queue[-1][1]
            for x in range(len(self.dicts[key].queue)-1,-1,-1):
                if self.dicts[key].queue[x][0] <= timestamp:
                    return self.dicts[key].queue[x][1]
                
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
