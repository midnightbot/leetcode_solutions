class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        ans = []

        maxs  = [nums[0]]

        for x in nums[1:]:
            maxs.append(max(maxs[-1], x))

        for x in range(len(nums)):
            ans.append(nums[x] + maxs[x])

        

        return list(accumulate(ans))
