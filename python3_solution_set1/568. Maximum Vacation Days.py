##ss
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        ##dp[i][j] be the max vacation days I can get completing week 1..i and being now in city j
        reachflights = {}
        for x in range(len(flights)):
            reachflights[x] = [x]
            
        for x in range(len(flights)):
            for y in range(len(flights[0])):
                if flights[x][y] == 1:
                    reachflights[y].append(x)
                    
        #print(reachflights)
        #print(len(flights),len(flights[0]),len(days),len(days[0]))
        dp = [[-1 for x in range(len(flights))] for y in range(len(days[0]))]
        
        dp[0][0] = days[0][0]
        for x in range(0,len(dp[0])):
            if flights[0][x] == 1:
                dp[0][x] = days[x][0]
         
        for x in range(1,len(dp)):
            for y in range(0,len(dp[0])):
                maxs = -float('inf')
                for m in reachflights[y]:
                    if (flights[m][y]==1 and dp[x-1][m]!=-1) or (m == y and dp[x-1][m]!=-1):
                        maxs = max(maxs, dp[x-1][m])
                    
                #print(x,y)    
                dp[x][y] = (maxs + days[y][x])
                
        ans = 0
        for x in range(len(dp[0])):
            ans = max(ans,dp[len(dp)-1][x])
            
        #return ans
        #self.print_dp(dp)
        return ans
        
    def print_dp(self,dp):
        
        for x in range(len(dp)):
            print(dp[x])
