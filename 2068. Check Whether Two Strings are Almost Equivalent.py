class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        compare = [3]*26
        print(compare)
        
        
        word1f = [0]*26
        word2f = [0]*26
        
        for x in range(len(word1)):
            word1f[ord(word1[x])-ord('a')]+=1
            word2f[ord(word2[x])-ord('a')]+=1
        print(word1f,word2f)    
        for x in range(len(word1f)):
            word1f[x] = abs(word1f[x]-word2f[x])
            
        for x in range(26):
            if word1f[x]>compare[x]:
                return False
            
            
        return True
            
        
            
