##ss
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        seen = set()
        
        for x,y in ranges:
            
            for it in range(x,y+1):
                seen.add(it)
                
        
        for x in range(left, right+1):
            if x not in seen:
                return False
            
        return True
        
