##ss
class Solution:
    def secondHighest(self, s: str) -> int:
        
        seen = set()
        
        for x in s:
            if ord('0') <= ord(x) <= ord('9'):
                seen.add(int(x))
                
        if len(seen) < 2:
            return -1
        
        else:
            seen = list(seen)
            seen = sorted(seen)
            
            return seen[-2]
        
