class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for x in range(len(nums)):
            count = nums.count(nums[x])
            if count==1:
                return nums[x]
        
        
