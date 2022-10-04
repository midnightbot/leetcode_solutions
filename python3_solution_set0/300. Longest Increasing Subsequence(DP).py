class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ans = [1] * len(nums)
        ##ans[k] -> LIS ending at index k
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(1+ans[j],ans[i])
                    
        return max(ans)
        
        
