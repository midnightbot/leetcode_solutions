class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        ans = 0
        nums = [format(x,'b') for x in nums]
        maxs = max([len(x) for x in nums])
        n = len(nums)
        for x in range(len(nums)):
            diff = maxs - len(nums[x])
            nums[x] = "".join(['0' for it in range(diff)]) + nums[x]

        comp = [0 for x in range(maxs)]

        for x in nums:
            for it in range(len(x)):
                if x[it] == '1':
                    comp[it]+=1
        comp1 = [n - x for x in comp]
        for i in range(len(comp)):
            ans+= comp[i] * comp1[i]



        return ans
