class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min([nums[x+1] - nums[x] for x in range(len(nums)-1)])
