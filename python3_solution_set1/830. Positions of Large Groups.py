class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        grps = []
        c = 1
        
        for x in range(1,len(s)):
            if s[x] == s[x-1]:
                c+=1
                
            else:
                if c>=3:
                    grps.append([x-c,x-1])
                c = 1
                
        
        if c>=3:
            grps.append([x-c+1,x])
        return grps
        
