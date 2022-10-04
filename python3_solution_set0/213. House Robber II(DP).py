class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp1 =  self.robbing(0,nums[0:len(nums)-1],{})
        temp2 = self.robbing(0,nums[1:len(nums)],{})
                                    
        return max(temp1, temp2)
    
    def robbing(self,i,nums,memo={}):
        
        if i>=len(nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        ans = max(self.robbing(i+1,nums,memo),self.robbing(i+2,nums,memo)+nums[i])
        
        memo[i] = ans
        return memo[i]
