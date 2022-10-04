##ss
##naive solution
class Solution:
    def maxPower(self, s: str) -> int:
        
        ans = 1
        
        for x in range(len(s)):
            if len(s) - x < (ans):
                break
                
            for y in range(x,len(s)):
                if s[y] != s[x]:
                    break
                    
            if y == len(s)-1 and s[len(s)-1] == s[len(s)-2]:
                ans = max(ans,y-x+1)
            else:
                ans = max(ans, y-x)
            
        return ans
        
