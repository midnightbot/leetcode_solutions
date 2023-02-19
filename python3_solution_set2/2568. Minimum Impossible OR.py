class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:

        nums = set(nums)

        for x in range(200):
            if 2**x not in nums:
                return 2**x
