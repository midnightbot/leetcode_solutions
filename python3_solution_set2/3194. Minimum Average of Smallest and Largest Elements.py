class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()
        ans = []
        
        for x in range(len(nums)//2):
            ans.append((nums[x]+nums[-1-x])/2)
        return min(ans)
        
