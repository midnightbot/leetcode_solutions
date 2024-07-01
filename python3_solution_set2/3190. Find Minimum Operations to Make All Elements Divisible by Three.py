class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        return sum([0 if nums[x]%3==0 else 1 for x in range(len(nums))])
        
