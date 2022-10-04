##Solution 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        for x in range(len(s2)-len(s1)+1):
            s = s2[x:x+len(s1)]
            #print(sorted(s),sorted(s1))
            if sorted(s) == sorted(s1):
                return True
            
        return False
        
