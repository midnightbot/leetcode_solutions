##ss
class AllOne:

    def __init__(self):
        
        self.mins = float('inf')
        self.maxs = 0
        self.freq = {}
        self.fmaps = defaultdict(set)
        

    def inc(self, key: str) -> None:
        #print(self.mins, self.maxs, self.freq,self.fmaps,"inc")
        
        self.freq[key] = self.freq.get(key,0) + 1
        if self.freq[key] > self.maxs:
            
            self.maxs = self.freq[key]

        if self.freq[key] == 1:
            self.fmaps[1].add(key)
            self.mins = 1
        else:
            self.fmaps[self.freq[key]-1].remove(key)
            if len(self.fmaps[self.freq[key]-1]) == 0 and self.mins == self.freq[key]-1:
                self.mins = self.freq[key]
            self.fmaps[self.freq[key]].add(key)
        

    def dec(self, key: str) -> None:
        #print(self.mins, self.maxs, self.freq,self.fmaps,"dec")
        self.freq[key]-=1
        
        if self.freq[key] == 0:
            self.fmaps[1].remove(key)
            
            if self.maxs == 1 and len(self.fmaps[1]) == 0:
                self.maxs = 0
            
            if self.mins == 1 and len(self.fmaps[1]) == 0 and self.maxs == 0:
                self.mins = self.freq[key]
                
            elif self.mins == 1 and len(self.fmaps[1]) == 0:
                self.mins = float('inf')
                for x in self.fmaps:
                    if len(self.fmaps[x]) > 0:
                        self.mins = min(self.mins, x)
                    
        else:
            self.fmaps[self.freq[key]+1].remove(key)
            self.fmaps[self.freq[key]].add(key)
            
            if len(self.fmaps[self.freq[key] + 1]) == 0:
                if self.maxs == self.freq[key] + 1:
                    self.maxs = self.freq[key]
                    
            self.mins = min(self.mins, self.freq[key])

    def getMaxKey(self) -> str:
        #print(self.mins, self.maxs, self.freq,self.fmaps,"maxkey")
        if len(self.fmaps[self.maxs]) == 0:
            return ""
        else:
            return list(self.fmaps[self.maxs])[0]
        

    def getMinKey(self) -> str:
        #print(self.mins, self.maxs, self.freq,self.fmaps,"minkey")
        if len(self.fmaps[self.mins]) == 0:
            return ""
        else:
            return list(self.fmaps[self.mins])[0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
