class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        n_colors = len(costs[0])
        #print(n_colors)
        if len(costs) == 1:
            return min(costs[0])
        dp = [[0 for x in range(n)] for y in range(n_colors)] 

        temp = costs [0]
        for x in range(n_colors): ##initialization
            
            dp[x][0] = temp[x]
            #print(dp)
            
        for x in range(1,n):##n_color
            for y in range(n_colors):##1,n
                #print(dp[x][y])
                mins = float('inf')
                for z in range(n_colors):
                    if z!=y and dp[z][x-1] < mins:
                        #print(dp[z][y-1])
                        mins = dp[z][x-1]
                     
                dp[y][x] = mins + costs[x][y]
                
        print(dp)
        mins = float('inf')
        for x in range(len(dp)):
            if dp[x][len(dp[0])-1] < mins:
                mins = dp[x][len(dp[0])-1]
                
        return mins
                
                
        
                        
