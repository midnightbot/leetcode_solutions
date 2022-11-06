class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []
        zeros = []
        for x in range(n-1):
            if nums[x] == nums[x+1]:
                nums[x]*=2
                nums[x+1] = 0


        for x in nums:
            if x!=0:
                ans.append(x)
            else:
                zeros.append(x)

        return ans+zeros
