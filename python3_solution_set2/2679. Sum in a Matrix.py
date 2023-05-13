class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        for x in range(len(nums)):
            nums[x].sort()

        ans = 0 
        nums = [x for x in zip(*nums)]
        for x in nums:
            ans+=max(x)
        return ans
