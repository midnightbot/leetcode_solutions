class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxs = max(nums)
        ans = nums.index(maxs)
        
        for x in range(len(nums)):
            
            if nums[x]!=maxs and nums[x] * 2 > maxs:
                return -1
            
        return ans
        
        
