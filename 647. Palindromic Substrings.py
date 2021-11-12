class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for x in range(len(s)):
            for y in range(x,len(s)):
                if s[x:y] == s[y:x:-1]:
                    count+=1
                    
        return count
        
