##ss
class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        self.root = Node()
        wrds = [[len(x),x[::-1]] for x in words]
        wrds = sorted(wrds, reverse = True,key = lambda x:x[0])
        #print(wrds)
        c = 0
        for y,x in wrds:
            tmp = self.insert(x)
            if tmp !=0: ## if a word is completely overlapped by suffix of some word, then no characters are to be added else word + "#" is added to the ans
                c+=len(x)+1
            
            #print(c, "--")
        return c
        
        
        
        
    def insert(self, word: str) -> None:
        ptr = self.root
        res = 0
        for x in word:
            if x not in ptr.children:
                res+=1
                ptr.children[x] = Node()
                
            ptr = ptr.children[x]
            
        ptr.isend = True
        return res
        
