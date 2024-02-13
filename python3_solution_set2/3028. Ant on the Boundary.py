class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        return list(accumulate(nums)).count(0)
        
