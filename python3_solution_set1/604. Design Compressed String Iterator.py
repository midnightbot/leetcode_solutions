##ss
class StringIterator:

    def __init__(self, compressedString: str):
        
        self.str = compressedString
        self.chr = []
        self.rep = []
        
        
        reps = ""
        chrs = ""
        for x in range(len(compressedString)):
            if ord(compressedString[x])>=ord('0') and ord(compressedString[x])<=ord('9'):
                reps+=compressedString[x]
                
            else:
                self.chr.append(chrs)
                self.rep.append(reps)
                chrs = compressedString[x]
                reps = ""
               
        self.chr.append(chrs)
        self.rep.append(int(reps))
        
        self.chr = self.chr[1:]
        self.rep = self.rep[1:]
        
        self.rep = [int(x) for x in self.rep]
        #print(self.chr,self.rep)
        self.pos = 0
                
        

    def next(self) -> str:
        #print(self.pos,self.hasNext())
        if self.hasNext():
            if self.rep[self.pos] > 0:
                self.rep[self.pos]-=1
                return self.chr[self.pos]

            elif self.rep[self.pos] == 0:
                self.pos+=1
                if self.hasNext():
                    self.rep[self.pos]-=1

                    return self.chr[self.pos]
            
        else:
            return " "
        
        return " "

    def hasNext(self) -> bool:
        
        if self.pos >= len(self.chr):
            return False
        
        elif self.pos == len(self.chr)-1 and self.rep[self.pos] == 0:
            return False
        
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
