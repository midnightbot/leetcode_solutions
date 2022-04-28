##ss
import bisect
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        flowers1 = sorted([x[0] for x in flowers])
        flowers2 = sorted([x[1] for x in flowers])
        
        return [bisect.bisect_right(flowers1,x) - bisect.bisect_left(flowers2,x) for x in persons]
        
        
        
