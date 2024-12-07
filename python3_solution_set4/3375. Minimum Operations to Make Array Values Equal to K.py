class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unq = len(set(nums))
        if unq == 1 and nums[0] == k:
            return 0

        if k >= max(nums):
            return -1

        if k < min(nums):
            return unq
        
        if k == min(nums):
            return max(0,unq-1)

        return -1
