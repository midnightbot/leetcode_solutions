class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxs = 0
        counter = 0
        if len(nums)==1 and nums[0]==1:
            return 1
        for x in range(len(nums)):
           
            if nums[x]==1:
                counter+=1
            else:
                if counter > maxs:
                    maxs = counter
                    
                counter = 0
        if counter > maxs:
            maxs = counter
        return maxs
            
        
