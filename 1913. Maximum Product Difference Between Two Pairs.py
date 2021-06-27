class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        k = len(nums)
        return ((nums[k-1]*nums[k-2]) - (nums[0]*nums[1]))
        
