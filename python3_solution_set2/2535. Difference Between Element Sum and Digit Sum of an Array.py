class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        return sum(nums) - sum([int(x) for y in nums for x in str(y)])
