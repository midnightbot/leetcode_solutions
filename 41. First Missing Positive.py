class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for x in range(1,301):
            if x not in nums:
                return x
        
