##Solution 1
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        dp = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                dp[x][y] = matrix[x][y]
            
        for x in range(1,len(matrix)):
            for y in range(1,len(matrix[0])):
                if dp[x][y]!=0:
                    dp[x][y]+=min(dp[x-1][y-1],dp[x-1][y],dp[x][y-1])
                    
                
                    
        count = 0
        print(dp)
        for x in range(len(dp)):
            count+=sum(dp[x])
            
        return count
##Solution 2 (Same as solution 1, only change is using matrix as dp array)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        

        for x in range(1,len(matrix)):
            for y in range(1,len(matrix[0])):
                if matrix[x][y]!=0:
                    matrix[x][y]+=min(matrix[x-1][y-1],matrix[x-1][y],matrix[x][y-1])
  
        count = 0
        
        for x in range(len(matrix)):
            count+=sum(matrix[x])
            
        return count
