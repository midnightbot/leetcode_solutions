##ss
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        
        ptr = self.root
        
        for x in range(len(word)):
            if word[x] not in ptr.children:
                ptr.children[word[x]] = Trie()
                
            ptr = ptr.children[word[x]]
            
        ptr.end = True
            

    def search(self, word: str) -> bool:
        
        def expand(pos,root):
            ptr = root
            
            for x in range(pos,len(word)):
                
                if word[x] == '.':
                    for child in ptr.children.values():
                        if expand(x+1,child):
                            return True
                        
                    return False
                        
                else:
                    if word[x] not in ptr.children:
                        return False
                    
                    ptr = ptr.children[word[x]]
                    
            return ptr.end
                        
        return expand(0,self.root)
                        
                        
        
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
