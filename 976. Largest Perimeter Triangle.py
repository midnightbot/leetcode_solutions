class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        for x in range(len(nums)-3,-1,-1):
            if nums[x]+nums[x+1] > nums[x+2]:
                return sum(nums[x:x+3])
            
            
        return 0
        
        
        
