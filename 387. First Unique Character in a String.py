class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        
        for x in range(len(s)):
            if s[x] not in s[:x] and s[x] not in s[x+1:]:
                return x
        
        return -1
        
