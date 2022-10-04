class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        maxs = -float('inf')
        for x in range(len(nums)-1):
            temp = max(nums[x+1:len(nums)]) - nums[x]
            if temp > maxs:
                maxs = temp
                
        if maxs <= 0:
            return -1
        else:
            return maxs
            
        
