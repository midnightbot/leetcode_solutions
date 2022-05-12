from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        l = set(list(permutations(nums)))
        
        return l
        
        
