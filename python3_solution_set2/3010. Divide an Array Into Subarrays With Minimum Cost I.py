class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans= sum(nums[:3])
        
        for x in range(1, len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] + nums[0] < ans:
                    ans = nums[x] + nums[y] + nums[0]

        return ans
        
