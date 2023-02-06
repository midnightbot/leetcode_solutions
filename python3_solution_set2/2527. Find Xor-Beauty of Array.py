class Solution:
    def xorBeauty(self, nums: List[int]) -> int:

        ## (nums[i] OR nums[j]) AND nums[k]
        ans = 0
        for x in nums:
            ans^=x
        return ans
