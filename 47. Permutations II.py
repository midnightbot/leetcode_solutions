## Same as 46. Permutations (Just use as set to store all the permutations, as set does not allow duplicate entries)
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        l = set(list(permutations(nums)))
        
        return l
        
        
