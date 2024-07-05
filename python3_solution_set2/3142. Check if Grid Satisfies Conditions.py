class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        for x in range(n):
            for y in range(m):
                if x+1<n and grid[x][y]!=grid[x+1][y]:
                    return False
                if y+1<m and grid[x][y] == grid[x][y+1]:
                    return False

        return True
        
