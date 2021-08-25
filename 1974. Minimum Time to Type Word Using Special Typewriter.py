class Solution:
    def minTimeToType(self, word: str) -> int:
        
        ans = 0
        current = 'a'
        for x in range(len(word)):
            
            temp1 = abs(ord(current)-ord(word[x]))
            temp2 = abs(26-temp1)
            mins = min(temp1,temp2)
            #print(mins)
            ans += abs(mins)
            current = word[x]
            
            
            
            
        return ans+len(word)
            
            
        
