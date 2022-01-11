##ss
##Simple Trie question
class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = Node()
        
        for x in range(len(words)):
            self.insert(words[x])
         
        words = sorted(words)
        words = sorted(words, key = lambda x : (-len(x)))
        #print(words)
        ##words sorted by len and lexical order
        
        for x in range(len(words)):
            var = 0
            for y in range(1,len(words[x])+1):
                if self.search(words[x][:y]):
                    var+=1
                    continue
                    
                else:
                    break
            #print(words[x],var)        
            if var == len(words[x]):
                return words[x]
        return ""
        
    def insert(self,word):
        ptr = self.root
        
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
                
            ptr = ptr.children[letter]
            
        ptr.isend = True
    
    
    
    def search(self,word):
        ptr = self.root
        
        for letter in word:
            if letter not in ptr.children:
                return False
            
            ptr = ptr.children[letter]
            
        if ptr.isend:
            return True
        return False
        
