class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        print(nums)
        if len(nums)==1:
            return nums[0]
        for x in range(0,len(nums)-1,2):
            print(x)
            if nums[x]!=nums[x+1]:
                return nums[x]
            
            elif x==len(nums)-3:
                return nums[x+2]
            
        
