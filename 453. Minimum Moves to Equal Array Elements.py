class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        count =0 
        for x in range(len(nums)):
            count+=nums[x]-nums[0]
            
        return count
            
        
            
        
