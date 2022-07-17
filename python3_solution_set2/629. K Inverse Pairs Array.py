##Solution 1(TLE)
class Solution:
    def kInversePairs(self, n: int, d: int) -> int:
        mods = 10**9 + 7
        
        ## nums[i] > nums[j]
        ## [1,2..n] -> arr
        ## should have exactly k inverted pairs
        
        @cache
        def find_ans(indx, k):
            #print("inside")
            if indx <= n and k == 0:
                return 1
            elif indx==n and k!=0:
                return 0
            else:
                #print("here",indx,k)
                ans = 0
                for x in range(min(k+1,indx+1)):
                    #print(x)
                    ans+=find_ans(indx+1,k-x)
                    ans = ans % mods
                    
                return ans%mods
            
        return find_ans(0,d)%mods
                    
## Solution 2
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        mods = 10**9 + 7
        
        dp = [[0 for x in range(k+1)] for y in range(n+1)]
        dp[0][0] = 1
        
        for x in range(1,n+1):
            for y in range(k+1):
                if y == 0:
                    dp[x][y]+=dp[x-1][0]
                    
                else:
                    dp[x][y] += dp[x][y-1] + dp[x-1][y]
                    
                    if y-x>=0:
                        dp[x][y] -= dp[x-1][y-x]
                dp[x][y] = dp[x][y] % mods
                
        return dp[-1][-1]
