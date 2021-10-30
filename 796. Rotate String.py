class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        
        for x in range(len(s)):
            s = s[len(s)-1] + s[0:len(s)-1]
            if s == goal:
                return True
            
            
        return False
        
