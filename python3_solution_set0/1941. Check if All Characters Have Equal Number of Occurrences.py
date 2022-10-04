##ss
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        ans = [0 for x in range(26)]
        
        for x in range(len(s)):
            ans[ord(s[x])-ord('a')]+=1
            
        temp = -1
        
        for x in range(len(ans)):
            if ans[x]!=0 and temp == -1:
                temp = ans[x]
                
            elif ans[x]!=0 and temp!=-1 and ans[x]!=temp:
                return False
            
        return True
                
