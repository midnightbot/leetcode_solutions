##ss
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ##to make it strictly increasing
        
        ## nums[i] < nums[i+1]
        
        c = 0 
        
        for x in range(1,len(nums)):
            if nums[x] > nums[x-1]:
                continue
                
            else:
                c+= nums[x-1] - nums[x] + 1
                nums[x] = nums[x-1] + 1
                
        return c
        
