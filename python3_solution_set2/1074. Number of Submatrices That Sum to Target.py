class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        ##(x1,y1) top left corner of the matrix
        ##(x2,y2) bottom right corner of the matrix
        
        r = len(matrix)
        c = len(matrix[0])
        
        dp = [[0 for x in range(c+1)]for y in range(r+1)]
        
        for x in range(1,r+1):
            for y in range(1,c+1):
                dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + matrix[x-1][y-1]
                
                
        ans = 0
        
        for x in range(1,r+1):
            for y in range(x,r+1):
                
                temp = {}
                temp[0] = 1
                
                for cols in range(1,c+1):
                    cu = dp[y][cols] - dp[x-1][cols]
                    ans += temp.get(cu-target,0)
                    temp[cu] = temp.get(cu,0) + 1
        
        return ans
                        
            
