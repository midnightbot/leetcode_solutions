class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        if len(s) < 3:
            return 0
        
        ans = 0
        for x in range(len(s)-3+1):
            
            if len(set(s[x:x+3])) == 3:
                #print(s[x:x+3])
                ans+=1
                
        return ans
