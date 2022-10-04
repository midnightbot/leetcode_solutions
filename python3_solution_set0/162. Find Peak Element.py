class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
            
        for x in range(0,len(nums)-1,1):
            if x==0 and nums[0]>nums[1]:
                return 0
           
            elif  nums[x]>nums[x-1] and nums[x]>nums[x+1]:
                return x
            
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        
