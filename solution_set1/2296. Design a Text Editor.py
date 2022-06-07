##ss
class TextEditor:
    ## simple string solution, as text size is 0<=size<=40, no problem to directly use a string
    def __init__(self):
        
        self.s = ""
        self.indx = 0
        

    def addText(self, text: str) -> None:
        
        self.s = self.s[0:self.indx] + text + self.s[self.indx:]
        self.indx+=len(text)
        

    def deleteText(self, k: int) -> int:
        
        if k > self.indx:
            self.s = self.s[self.indx:]
            temp = self.indx
            self.indx = 0
            return temp

        else:
            self.s = self.s[0:self.indx - k] + self.s[self.indx:]
            self.indx-=k
            return k
            
        

    def cursorLeft(self, k: int) -> str:
        
        self.indx = max(0,self.indx-k)
        return self.s[max(0,self.indx-10):self.indx]
        #return self.s[self.indx:min(len(self.s), self.indx+10)]
        

    def cursorRight(self, k: int) -> str:
        
        self.indx = min(self.indx+k, len(self.s))
        return self.s[max(0,self.indx-10):self.indx]
        #return self.s[self.indx:min(len(self.s), self.indx+10)]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
