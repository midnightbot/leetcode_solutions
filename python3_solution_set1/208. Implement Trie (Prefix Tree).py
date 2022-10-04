##ss
class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
        
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        ptr = self.root
        
        for x in word:
            if x not in ptr.children:
                ptr.children[x] = Node()
                
            ptr = ptr.children[x]
            
        ptr.isend = True
        

    def search(self, word: str) -> bool:
        ptr = self.root
        for x in word:
            if x not in ptr.children:
                return False
            ptr = ptr.children[x]
            
        if ptr.isend:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for x in prefix:
            if x not in ptr.children:
                return False
            ptr = ptr.children[x]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
