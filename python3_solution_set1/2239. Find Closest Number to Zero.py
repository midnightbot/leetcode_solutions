##ss
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        diff  = float('inf')
        indx = -1
        
        for x in range(len(nums)):
            if abs(nums[x] - 0) < diff:
                diff = abs(nums[x] - 0)
                indx = x
                
            elif abs(nums[x] - 0) == diff and nums[x] > nums[indx]:
                indx = x
                
        return nums[indx]
        
