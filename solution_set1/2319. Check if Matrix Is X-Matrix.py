##ss
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        
        for x in range(n):
            if grid[x][x] == 0:
                return False
            
        for x in range(n):
            if grid[x][n-x-1] == 0:
                return False
        
        for x in range(n):
            for y in range(n):
                if x!=y and y!=n-x-1 and grid[x][y]!=0:
                    return False
        return True
