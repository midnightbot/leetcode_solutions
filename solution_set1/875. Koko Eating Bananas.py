##ss
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right-left) // 2
            hours = 0
            for x in range(len(piles)):
                hours+=(piles[x] // mid) + math.ceil((piles[x]%mid)/mid)
                
                if hours > h:
                    left = mid + 1
                    break
                
                    
            if hours <= h:
                right = mid
                
            else:
                left = mid + 1
                
                
        return left
        
