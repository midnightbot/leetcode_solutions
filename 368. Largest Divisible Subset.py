(Approach 1 : Time Limit Exceeded 27/48 Test Cases Passed)
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
            
            
            
            
        
            
            
