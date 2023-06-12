class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:

        ## collisions will not affect the problem
        for x in range(len(nums)):
            if s[x] == 'L':
                nums[x]-=d
            else:
                nums[x]+=d
        nums.sort()
        ans = 0
        pre = 0
        mods = 10**9+7
        for x in range(len(nums)):
            ans+= (x*nums[x] - pre)%mods
            pre+=nums[x]

        return ans%mods
