class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        return max(sum([1 if x>0 else 0 for x in nums]), sum([1 if x<0 else 0 for x in nums]))
