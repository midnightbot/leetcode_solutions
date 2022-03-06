##ss
class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        self.root = Node()
        
        
        for x in range(len(dictionary)):
            self.insert(dictionary[x])
        
        ans = []
        comp = sentence.split(" ")
        for x in comp:
            #print(self.startsWith(x))
            if self.startsWith(x)[0] == True:
                ans.append(self.startsWith(x)[1])
            else:
                ans.append(x)
                
        return " ".join(ans)
        
    def insert(self, word: str) -> None:
        ptr = self.root
        
        for x in word:
            if x not in ptr.children:
                ptr.children[x] = Node()
                
            ptr = ptr.children[x]
            
        ptr.isend = True
        
        
    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        root_made = ""
        for x in prefix:
            if ptr.isend:
                return True, root_made
            
            if x not in ptr.children:
                return False,False
            root_made += x
             
            ptr = ptr.children[x]
            
        if ptr.isend:
            return True, prefix
        else:
            return False,False
        
