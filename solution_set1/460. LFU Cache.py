##ss
from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.minfreq = 0
        self.dicts = defaultdict(int) ##key : value
        self.freq = defaultdict(OrderedDict) ## freq : {}
        
    def upd_freq(self, key, value = None):
        f = self.dicts[key]
        vals = self.freq[f].pop(key)
        
        if value is not None:
            vals = value
            
        self.freq[f+1][key] = vals
        self.dicts[key]+=1
        
        if self.minfreq == f and not self.freq[f]:
            self.minfreq+=1
            
        return vals
        
    def get(self, key: int) -> int:
        
        if key not in self.dicts:
            return -1
        
        
        return self.upd_freq(key)
        

    def put(self, key: int, value: int) -> None:
        
        if not self.capacity:
            return 
        
        if key in self.dicts:
            self.upd_freq(key,value)
            
        else:
            if len(self.dicts) == self.capacity:
                self.dicts.pop(self.freq[self.minfreq].popitem(last=False)[0])
                
            self.minfreq = 1 
            
            self.dicts[key] = 1
            self.freq[1][key] = value
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
