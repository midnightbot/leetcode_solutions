class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        def find_ans(x):
            for i in range(nums[x]+1):
                if i | (i+1) == nums[x]:
                    return i
            return -1

        return [find_ans(x) for x in range(len(nums))]
        
