##ss
##not optimized
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for x in range(0,len(nums)):
            if sum(nums[0:x]) == sum(nums[x+1:len(nums)]):
                return x
            
        return -1
        
