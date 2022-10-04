##ss
##Solution1 (Time Limit Exceeded 23/25 Test cases passed)
class LFUCache:
    ##least freq and then least recently used
    
    def __init__(self, capacity: int):
        self.dicts = {}
        self.freq = {}
        self.capacity = capacity
        #self.last_used = -1
        self.lru = {}
        self.time = 0
        
    def get(self, key: int) -> int:
        self.time+=1
        if key in self.dicts:
            #self.last_used = key
            self.lru[key] = self.time
            self.freq[key] = self.freq.get(key,0) + 1
            return self.dicts[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.time+=1
        
        if self.capacity > 0 or key in self.dicts:
            self.freq[key] = self.freq.get(key,0) + 1
            self.lru[key] = self.time
            if key in self.dicts:
                self.dicts[key] = value
                
            else:
                self.dicts[key] = value
                self.capacity-=1
        
        elif self.capacity == 0:
            mins = float('inf')
            curr_min = -1
            
            for x in self.freq:
                if self.freq[x] < mins:
                    mins = self.freq[x]
                    curr_min = x
                    
                elif self.freq[x] == mins and self.lru[curr_min] > self.lru[x]:
                    curr_min = x
            
            
                        
            if self.lru:
                self.lru.pop(curr_min)
                self.dicts.pop(curr_min)
                self.freq.pop(curr_min)
                self.dicts[key] = value

                self.freq[key] = 1
                
            
                self.lru[key] = self.time 
                

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

##Solution2 (Accepted)
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
