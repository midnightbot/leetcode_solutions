class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        def print_dp(dp):
            
            for x in range(len(dp)):
                print(dp[x])
                
        dp = [[0 for x in range(n+1)] for y in range(m+1)]
        ans = [[0 for x in range(n)] for y in range(m)]
        for x in range(1,m+1):
            for y in range(1,n+1):
                dp[x][y] = dp[x-1][y] + dp[x][y-1] + mat[x-1][y-1] - dp[x-1][y-1]
                
        
        #print_dp(dp)
        
        for x in range(m):
            for y in range(n):
                
                rl = max(0,x-k) + 1
                cl = max(0,y-k) + 1
                
                rr = min(m-1,x+k) + 1
                cr = min(n-1,y+k) + 1
                
                ans[x][y] = dp[rr][cr] - dp[rr][cl-1] - dp[rl-1][cr] + dp[rl-1][cl-1]
        
        return ans
