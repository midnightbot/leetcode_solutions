class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)

        dp = [[0 for x in range(n+1)]for y in range(m+1)]

        for x in range(1,n+1):
            dp[0][x] = sys.maxsize
        
        for x in range(1,m+1):
            for y in range(1,n+1):
                if s1[x-1] == s2[y-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                else:
                    dp[x][y] = dp[x-1][y] + 1

        mins = sys.maxsize//2
        end = -1

        for x in range(1,m+1):
            if dp[x][n] < mins:
                mins = dp[x][n]
                end = x - 1

        if mins == sys.maxsize//2:
            return ''
        else:
            
            return s1[end-mins+1:end+1]
