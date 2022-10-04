class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        
        for x in range(len(nums)):
            if x%10 == nums[x]:
                return x
            
        return -1
        
