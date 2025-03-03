class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return [0]*sum([1 if x%2==0 else 0 for x in nums]) + [1]*sum([0 if x%2==0 else 1 for x in nums])
        
