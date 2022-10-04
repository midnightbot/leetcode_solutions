##ss
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        ##do bfs but from buildings
        
        builds = 0
    
    
        reach_grid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        ans_grid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        n = len(grid[0])
        m = len(grid)
        def do_bfs(y0, x0):
            seen = [[0]*len(grid[0]) for _ in range(len(grid))]
            q = collections.deque([(y0, x0, 0)])
            while q:
                y, x, d = q.popleft()
                for yp, xp in {(y-1,x), (y+1, x), (y, x+1), (y, x-1)}:
                    if 0 <= yp < m and 0 <= xp < n and grid[yp][xp] == 0 and seen[yp][xp] == 0:
                        seen[yp][xp] = 1
                        ans_grid[yp][xp]+=d+1
                        reach_grid[yp][xp]+=1
                        q.append((yp,xp,d+1))
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    do_bfs(x,y)
                    
                    builds+=1
                   
                    
        ans = float('inf')
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if reach_grid[x][y] == builds and grid[x][y] == 0:
                    ans = min(ans, ans_grid[x][y])
                    
        return ans if ans!=float('inf') else -1
