class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ## opt(i,j) = min(opt(i-1,j),opt(i,j-1)) + value(i,j)
        ## just initialize first row and first column
        
        for i in range(1,len(grid)): ##initializing first column
            grid[i][0]+=grid[i-1][0]
        for j in range(1,len(grid[0])): ##initializing first row
            grid[0][j] +=grid[0][j-1]
            
            
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
                
        print(grid)       
        return grid[len(grid)-1][len(grid[0])-1]
        
        
        
