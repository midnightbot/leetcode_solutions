class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:

        nums = [[x, abs(x)] for x in nums]
        nums = sorted(nums, key = lambda x:x[1])
        nums = [x[0] for x in nums]
        return nums        
