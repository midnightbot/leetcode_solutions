class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        count  = 0
        
        if nums.count(0)>=1:
            return 0
        
        for x in range(len(nums)):
            if nums[x]<0:
                count+=1
                
                
        if count%2==0:
            return 1
        else:
            return -1
        
