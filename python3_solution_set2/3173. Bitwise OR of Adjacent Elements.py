class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [nums[x]|nums[x+1] for x in range(len(nums)-1)]
        
