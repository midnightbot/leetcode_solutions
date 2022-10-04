##ss
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        comapre = self.mask(chars)
        ans = 0
        for x in range(len(words)):
            if self.compare(self.mask(words[x]),comapre):
                ans+=len(words[x])
                
                
        return ans
        
        
        
        
    def mask(self,word1):
        ans = [0 for x in range(26)]
        for x in range(len(word1)):
            ans[ord(word1[x])-ord('a')]+=1
            
        return ans
        
        
    def compare(self,word1,word2):
        for x in range(26):
            if word2[x] < word1[x]:
                return False
            
            
        return True
        
