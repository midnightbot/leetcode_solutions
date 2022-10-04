##ss
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        ##same row and same column
        
        ##ans = total servers - isolated servers
        
        rowsum = [0 for x in range(len(grid))]
        colsum = [0 for x in range(len(grid[0]))]
        
        for x in range(len(grid)):
            rowsum[x] = sum(grid[x])
            
        for x in range(len(grid[0])):
            temp = 0
            for y in range(len(grid)):
                temp+=grid[y][x]
                
            colsum[x] = temp
            
        ans = 0
        total = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and rowsum[x] == 1 and colsum[y] == 1:
                    ans+=1
                    
                if grid[x][y] == 1:
                    total+=1
                    
        return total - ans
                    
                    
        
