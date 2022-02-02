class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return []
        
        word1 = self.find_dict(s[0:len(p)])
        word2 = self.find_dict(p)
        if self.match(word1,word2):
            ans.append(0)
            
        prev = s[0]
        #print(word1)
        for x in range(1,len(s)-len(p)+1):
            #print(prev,word1)
            word1[prev]-=1
            if word1[prev] == 0:
                word1.pop(prev)
                
            if s[x+len(p)-1] in word1:
                word1[s[x+len(p)-1]]+=1
                
            else:
                word1[s[x+len(p)-1]] = 1
                
                
            if self.match(word1,word2):
                ans.append(x)
                
            prev = s[x]
            
        return ans
        
        
        
    def find_dict(self,word):
        
        dicts = {}
        
        for x in word:
            if x in dicts:
                dicts[x]+=1
                
            else:
                dicts[x] = 1
                
        return dicts
                
                
    def match(self,word1,word2):
        
        return word1 == word2
        
