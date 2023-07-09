class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        ## for every starting index find the max subarray satisfying the conditions


        n = len(nums)
        ans = 0
        for x in range(n):
            m = 0
            j = x+1
            while j < n and nums[j] - nums[j-1] == (-1)**m:
                j+=1
                m+=1
            ans = max(ans, j-x)

        return ans if ans > 1 else -1
