class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        sums = 0
        for x in range(0,len(nums),2):
            sums+=nums[x]
            
        return sums
        
