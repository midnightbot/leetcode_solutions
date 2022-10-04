class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        for x in range(0,max(nums)+1):
            #c = 0
            var = False
            for y in range(len(nums)):
                if nums[y]>= x:
                    var = True
                    break
                    
            if var==True and x == (len(nums)-y):
                return x
            
            
        return -1
        
