class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        i = 1
        n = len(nums)
        c = 1
        ans = 1
        while i < n:
            if nums[i] > nums[i-1]:
                c+=1
            else:
                ans = max(ans, c)
                c = 1
            i+=1

        ans = max(ans, c)
        return ans

