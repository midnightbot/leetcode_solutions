##(Approach 1 : Time Limit Exceeded 27/48 Test Cases Passed)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums)
        dp = [[0 for x in range(len(nums))]for y in range(len(nums))]
        #print(dp)
        for x in range(len(dp)):
            dp[x][x] = 1
        for x in range(len(dp)):
            for y in range(x+1,len(dp)):
                maxs = -1
                for z in range(y+1):
                    if z!=y and nums[y]%nums[z] == 0:
                        maxs = max(maxs, 1 + dp[x][z])
                    
                    
                dp[x][y] = max(maxs,1)
                
        ans = []
        print(dp)
        for x in range(len(dp)):
            ans.append(max(dp[x]))
            
        index = ans.index(max(ans))
        finals = dp[index]
        print(finals)
        c = finals.index(max(finals))
        rets = []
        rets.append(nums[c])
        current = max(finals)
        for x in range(c-1,-1,-1):
            if finals[x]+1 == current and rets[len(rets)-1]%nums[x] == 0:
                rets.append(nums[x])
                current = finals[x]
                
        return (rets[::-1])
            
################################################################################################################################################################          
## Approach 2 (Passed)
##Similar to Approach1, the only change being rather than maintainting a 2-D dp array, created a 1-D dp array
##2-D dp array gives max subset for every set starting from i and ending at j
## But that is not necessary, instead we can have 1-D array and see if the element i is in the max subset or not
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums)
        
        dp  = [1 for x in range(len(nums))]
        
        for x in range(1,len(dp)):
            for y in range(x):
                if nums[x]%nums[y] == 0:
                    dp[x] = max(dp[x],1 + dp[y])
                    
        index = dp.index(max(dp))
        print(dp)
        ans  = []
        ans.append(nums[index])
        current = max(dp)
        for x in range(index-1,-1,-1):
            if dp[x]+1 == current and ans[len(ans)-1]%nums[x] == 0:
                ans.append(nums[x])
                current = dp[x]
                
        return ans[::-1]
 ##explanation : https://github.com/midnightbot/leetcode_solutions/blob/main/368.%20Largest%20Divisible%20Subset(DP).pdf
            
        
            
            
