from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        maxs = max(nums)
        counter = [0] * (maxs+1)
        
        for x in range(len(counter)):
            if x in nums:
                counter[x] = nums.count(x)
                
        print(counter)
        return self.robbing(0,counter,{})
    
    def robbing(self,i,counter,memo={}):
        
        if i>=len(counter):
            return 0
        
        if i in memo:
            return memo[i]
        
        ans = max(self.robbing(i+1,counter,memo),self.robbing(i+2,counter,memo)+counter[i]*i)
        
        memo[i] = ans
        return memo[i]
        
        
        
        
        
            
        
