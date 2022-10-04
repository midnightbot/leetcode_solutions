## Solution 1 (Using itertools import)
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = list(list(permutations(nums)))
        
        return l
            
        
