class Solution:
    def isGood(self, nums: List[int]) -> bool:

        return sorted(nums) == [x+1 for x in range(max(nums)-1)] + [max(nums) for x in range(2)]
