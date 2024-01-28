class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        s = s.lower()
        for x in range(1, len(s)):
            if s[x] != s[x-1]:
                ans+=1
                
        return ans
                
        
