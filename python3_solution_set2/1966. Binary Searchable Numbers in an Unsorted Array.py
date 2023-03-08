class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:

        ## l to r maxs array
        ## r to l mins array

        maxs = [nums[0]]
        n = len(nums)
        for x in range(1,n):
            maxs.append(max(maxs[-1], nums[x]))

        mins = [nums[-1]]
        for x in range(n-2,-1,-1):
            mins.append(min(mins[-1], nums[x]))
        mins = mins[::-1]
        ans = 0
        for x in range(len(nums)):
            if maxs[x] <= nums[x] and mins[x] >= nums[x]:
                ans+=1
        return ans
