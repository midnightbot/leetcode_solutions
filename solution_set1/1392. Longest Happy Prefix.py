##ss
class Solution:
    def longestPrefix(self, s: str) -> str:
        
        ##larest-prefix = suffix
        
        for x in range(len(s)-1,-1,-1):
            if s[0:x] == s[len(s) - x:]:
                return s[0:x]
        
