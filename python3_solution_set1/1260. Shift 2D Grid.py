##ss
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        def do_shift(grid):
            new_g = copy.deepcopy(grid)
            
            ##part1
            for x in range(m):
                for y in range(1,n):
                    new_g[x][y] = grid[x][y-1]
             
            for x in range(1,m):##part2
                new_g[x][0] = grid[x-1][-1]
                
            new_g[0][0] = grid[m-1][n-1] ##part3
            
            return new_g
        
        for x in range(k):
            grid = do_shift(grid)
            
        return grid
            
            
        
        
        
