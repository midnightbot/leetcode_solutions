class Solution:
    def partitionString(self, s: str) -> int:
        
        ans = 0
        
        seen = set()
        
        for x in s:
            if x not in seen:
                seen.add(x)
                
            else:
                ans+=1
                seen = {x}
        
        return ans+1
        
