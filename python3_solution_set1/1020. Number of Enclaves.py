class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        ##step1 remove all the islands that touch the boundary
        ##step2 find all the 1 cells that are remaining
        for x in range(len(grid[0])):
            if grid[0][x] == 1:
                self.bfs(grid,0,x)
        
        for x in range(len(grid)):
            if grid[x][0] == 1:
                self.bfs(grid,x,0)
                
        for x in range(len(grid[0])):
            if grid[len(grid)-1][x] == 1:
                self.bfs(grid,len(grid)-1,x)
                
        for x in range(len(grid)):
            if grid[x][len(grid[0])-1] == 1:
                self.bfs(grid,x,len(grid[0])-1)
                
        ans = 0
        
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                if grid[x][y] == 1:
                    
                    cells = self.bfs(grid,x,y)
                    ans+=cells
        return ans
        
        
    def bfs(self,grid,x,y):
        
        q = [[x,y]]
        cells = 0
        while q:
            cells+=len(q)
            for x in range(len(q)):
                
                node = q.pop(0)
                
                grid[node[0]][node[1]] = 0
                
                if node[0]-1>=0 and grid[node[0]-1][node[1]] == 1:
                    q.append([node[0]-1,node[1]])
                    grid[node[0]-1][node[1]] = 0
                    
                    
                if node[0] + 1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                    q.append([node[0]+1,node[1]])
                    grid[node[0]+1][node[1]] = 0
                    
                if node[1]-1 >=0 and grid[node[0]][node[1]-1] == 1:
                    q.append([node[0],node[1]-1])
                    grid[node[0]][node[1]-1] = 0
                    
                if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                    q.append([node[0],node[1]+1])
                    grid[node[0]][node[1]+1] = 0
        
        return cells
