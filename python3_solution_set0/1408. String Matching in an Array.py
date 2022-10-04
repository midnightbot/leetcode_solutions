class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ans = []
        words = list(sorted(words, key = len))
        #print(words)
        for x in range(len(words)):
            current = words[x]
            #print(current)
            for y in range(x+1,len(words)):
                if self.issubset(current,words[y]):
                    print(words[y])
                    ans.append(current)
                    break
        
        return ans
                    
                    
    def issubset(self,s1,s2):
        m = len(s1)
        n = len(s2)
        
        for i in range(n-m+1):
            if s2[i:i+m] == s1:
                return True
            
        return False
            
                
            
                
        
