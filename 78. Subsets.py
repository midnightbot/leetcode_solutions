##Solution 1 (Use of itertools)
from itertools import chain, combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        s = list(nums)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
        
