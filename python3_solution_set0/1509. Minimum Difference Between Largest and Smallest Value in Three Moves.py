class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        print(nums)
        ans = float('inf')
        if len(nums)<=4:
            return 0
        
        else:
            for i in range(4):
                ans = min(ans,nums[i-4]-nums[i])
                
            return ans
        
