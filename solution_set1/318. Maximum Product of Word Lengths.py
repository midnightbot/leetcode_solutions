##ss
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        ans = 0
        mask = []
        words = sorted(words, key = lambda x:len(x))
        #print(words)
        for x in range(len(words)):
            mask.append(self.find_mask(words[x]))
            
        for x in range(len(mask)):
            #print("ss")
            for y in range(len(mask)-1,-1,-1):
               
                if self.valid(mask[x],mask[y]):
                    #print("inside")
                    ans = max(ans, sum(mask[x]) * sum(mask[y]))
                    break
                    
                    
        return ans
        
        
    def find_mask(self,word):
        
        ans = [0 for x in range(26)]
        
        for x in word:
            ans[ord(x)-ord('a')]+=1
            
        return ans
    
    
    def valid(self,word1,word2):
        #print(word1,word2)
        for x in range(26):
            if word1[x] > 0 and word2[x] > 0:
                return False
            
        return True
        
