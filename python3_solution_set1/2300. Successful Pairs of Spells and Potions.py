##ss
import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions = sorted(potions)
        n = len(potions)
        return [n-bisect.bisect_left(potions,success/x) for x in spells]
       
