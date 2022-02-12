class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            diff = max(nums) - min(nums)
        
        else:
            diff = (max(nums) - min(nums)) - 2 * k
            
            
        return max(0,diff)
            
        
