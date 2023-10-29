class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans += len(set(nums[i:j+1]))**2
        return ans
        
