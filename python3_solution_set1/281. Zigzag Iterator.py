##ss
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        
        self.v1 = v1
        self.v2 = v2
        
        self.i = 0
        self.j = 0
        self.odd = 0

    def next(self) -> int:
        
        if self.odd == 0 and self.i < len(self.v1):
            self.i+=1
            self.odd+=1
            self.odd = self.odd % 2
            return self.v1[self.i - 1]
            
        elif self.odd == 0 and self.i >= len(self.v1):
            if self.j < len(self.v2):
                self.j+=1
                self.odd+=1
                self.odd = self.odd % 2
                return self.v2[self.j - 1]
            
            
        elif self.odd == 1 and self.j < len(self.v2):
            self.j+=1
            self.odd+=1
            self.odd = self.odd % 2
            return self.v2[self.j - 1]
            
        elif self.odd == 1 and self.j >= len(self.v2):
            if self.i < len(self.v1):
                self.i+=1
                self.odd+=1
                self.odd = self.odd % 2
                return self.v1[self.i - 1]
            
        
        

    def hasNext(self) -> bool:
        
        if self.i < len(self.v1) or self.j < len(self.v2):
            return True
        
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
