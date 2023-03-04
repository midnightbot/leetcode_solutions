class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        ans = 0

        mins = -1
        maxs = -1
        l = -1

        for x in range(len(nums)):

            if nums[x] < minK or nums[x] > maxK:
                l = x

            if nums[x] == minK:
                mins = x
            if nums[x] == maxK:
                maxs = x

            ans+= max(0, min(mins, maxs)-l)
        return ans
        
