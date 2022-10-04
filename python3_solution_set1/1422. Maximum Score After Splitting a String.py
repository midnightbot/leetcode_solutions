##ss
class Solution:
    def maxScore(self, s: str) -> int:
        
        left = 0
        right = s.count("1")
        
        ans = 0
        
        for x in range(len(s)-1):
            
            if s[x] == "0":
                left+=1
                
            elif s[x] == "1":
                right-=1
                
            ans = max(ans,left+right)
            
        #ans = max(ans,s.count("0"))
        return ans
        #ans = m
        
