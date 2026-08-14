class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum([nums[x] if x%2==0 else -nums[x] for x in range(len(nums))])
        
