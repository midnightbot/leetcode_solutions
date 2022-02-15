##ss
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        ##step 1 is to remove all islands touching boundary
        ##step2 now count number of islands
        
        for x in range(len(grid[0])):
            if grid[0][x] == 0:
                self.bfs(grid,0,x)
        
        for x in range(len(grid)):
            if grid[x][0] == 0:
                self.bfs(grid,x,0)
                
        for x in range(len(grid[0])):
            if grid[len(grid)-1][x] == 0:
                self.bfs(grid,len(grid)-1,x)
                
        for x in range(len(grid)):
            if grid[x][len(grid[0])-1] == 0:
                self.bfs(grid,x,len(grid[0])-1)
                
        ans = 0
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                if grid[x][y] == 0:
                    ans+=1
                    self.bfs(grid,x,y)
                    
        return ans
        
    def bfs(self,grid,x,y):
        
        q = [[x,y]]
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                grid[node[0]][node[1]] = 1
                
                if node[0]-1>=0 and grid[node[0]-1][node[1]] == 0:
                    q.append([node[0]-1,node[1]])
                    grid[node[0]-1][node[1]] = 1
                    
                    
                if node[0] + 1 < len(grid) and grid[node[0]+1][node[1]] == 0:
                    q.append([node[0]+1,node[1]])
                    grid[node[0]+1][node[1]] = 1
                    
                if node[1]-1 >=0 and grid[node[0]][node[1]-1] == 0:
                    q.append([node[0],node[1]-1])
                    grid[node[0]][node[1]-1] = 1
                    
                if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 0:
                    q.append([node[0],node[1]+1])
                    grid[node[0]][node[1]+1] = 1
                    
        
        
