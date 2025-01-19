class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0

        for indx,x in enumerate(nums):
            start = max(0, indx - x)
            ans+= sum(nums[start:indx+1])

        return ans
        
