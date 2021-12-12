##ss
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        
        ##simple dynamic programming
        ##dp[n] be number of ways n people can shake hand following the condition
        
        dp = [0 for x in range((num_people)+1)]
        
        dp[0] = 1
        dp[1] = 0
        dp[2] = 1
        
        
        ##dp[6] = (dp[4]*dp[0]+dp[2]*dp[2]+dp[0]*dp[4])
        
        for x in range(4,num_people+1,2):
            make = x - 2
            ans = 0
            #print(x,make)
            for y in range(make,-1,-2):
            
                #print(y,make-y)
                ans+=dp[y]*dp[make-y]
                #print(ans)
                
            dp[x] = ans%(pow(10,9)+7)
            
        return dp[num_people]%(pow(10,9)+7)
        
        
        
