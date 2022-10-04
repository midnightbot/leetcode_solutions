##ss
##Solution 1 (Time Limit Exceeded) Using Trie
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        self.n = -1
        
        self.result = []
        
        for x in range(len(words)):
            self.n = max(self.n,len(words[x]))
            
        self.expand(words,"",0)
        return self.result
            
    def expand(self,words,curr,joined):
        #print(curr)
        if curr in words and joined>=2:
            
            self.result.append(curr)
            
            
        if len(curr) < self.n:
            
            for x in range(len(words)):
                
                self.expand(words,curr+words[x],joined+1)
                
        
