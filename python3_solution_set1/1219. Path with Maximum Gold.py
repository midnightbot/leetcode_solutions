class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        ##left, right, up, down
        
        ##find all paths and then take max
        
        self.result = 0
        m = len(grid)
        n = len(grid[0])
        movesx = [1,-1,0,0]
        movesy = [0,0,1,-1]
        
        def expand(x,y,visited,thisans):
            if x<0 or x == m or y <0 or y == n or grid[x][y] == 0 or tuple([x,y]) in visited:
                return thisans
            
            
            visited.add(tuple([x,y]))
            ans = 0
            for z in range(4):
                ans = max(ans, expand(x+movesx[z],y+movesy[z],visited,thisans+grid[x][y]))
                
            visited.remove(tuple([x,y]))
            return ans
                
        for x in range(m):
            for y in range(n):
                if grid[x][y]!=0:
                    self.result = max(self.result, expand(x,y,set(),0))
                   
        return self.result
                
