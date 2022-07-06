##ss
class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        n = len(s)
        c = 0
        for x in range(n//2):
            if s[x]!=s[-1-x]:
                c+=1
                
        return c in [0,1,2]
        
