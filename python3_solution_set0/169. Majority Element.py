class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        temp = int(len(nums)/2)
        nums = sorted(nums)
        if len(nums) == 1:
            return nums[0]
        for x in range(len(nums)-1):
            if nums[x] == nums[temp]:
                return nums[x]
        
