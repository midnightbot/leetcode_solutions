class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for x in range(0,n-2):
            for y in range(x,n-1):
                for z in range(y,n):
                    if nums[x]!=nums[y] and nums[x]!=nums[z] and nums[y]!=nums[z]:
                        ans+=1

        return ans
