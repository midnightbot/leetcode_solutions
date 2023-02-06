
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])


        dicts = {x:set() for x in range(m)}
        ans = 0

        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    dicts[y].add((x))
                    
        for x in range(m-1):
            for y in range(x+1,m):
                temp = dicts[x].intersection(dicts[y])
                k = len(temp)
                ans+=k*(k-1)//2
        return ans

        




