class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        count = 0
        nums = sorted(nums,reverse=True)
        current = nums[0]
        
        for x in range(len(nums)-1):
            if count==2:
                return current
            if nums[x+1]<nums[x] and count!=2:
                count+=1
                current = nums[x+1]
                
        if count==2:
            return current
        else:
            return max(nums)
            
        
        
