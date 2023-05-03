class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        ## either add 0 or 2*k

        ans = float('inf')
        nums.sort()
        ans = min(ans, nums[-1] - nums[0])

        for x in range(len(nums)-1):
            maxs = max(nums[-1], nums[x] + 2*k)
            mins = min(nums[x+1], nums[0] + 2*k)
            ans = min(ans, maxs - mins)



        return ans
