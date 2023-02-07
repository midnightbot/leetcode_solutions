class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        ans  = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]!=0:
                    ans+=(grid[x][y]*4 + 2)

                if x!=0:
                    ans-= min(grid[x][y], grid[x-1][y])*2


                if y!=0:
                    ans-=min(grid[x][y], grid[x][y-1])*2

        return ans
