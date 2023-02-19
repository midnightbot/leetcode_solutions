class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums = sorted(nums)

        ans = 0
        for x in range(len(nums)-1,-1,-1):
            curr = nums[x]

            indx1 = bisect.bisect_left(nums, lower - curr, 0, x)
            indx2 = bisect.bisect_right(nums, upper - curr, 0, x)

            ans+= indx2 - indx1

        return ans


        
