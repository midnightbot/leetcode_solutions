class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum([1 if nums[x] < k else 0 for x in range(len(nums))])
        
