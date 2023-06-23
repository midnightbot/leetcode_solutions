class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        for x in range(n):
            for y in range(x+1, n):
                diff = nums[y] - nums[x]
                memo[(y,diff)] = memo.get((x,diff), 1) + 1

        return max(memo.values()) 
        
