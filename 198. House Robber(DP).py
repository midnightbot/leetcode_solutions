class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robbing(0,nums,{})
        
        
        
    def robbing(self,i,nums,memo={}):
        
        if i>=len(nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        ans = max(self.robbing(i+1,nums,memo),self.robbing(i+2,nums,memo)+nums[i])
        
        memo[i] = ans
        return memo[i]
        
