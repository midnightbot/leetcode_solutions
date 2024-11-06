class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            indx = nums.index(min(nums))
            nums[indx]*=multiplier

        return nums
        
