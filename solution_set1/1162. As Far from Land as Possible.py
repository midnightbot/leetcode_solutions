##ss
##simple bfs
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        ##manhattan dist
        
        newg = [[0 for x in range(len(grid[0]))]for y in range(len(grid))]
        
        q = []
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    q.append((0,x,y))
                    visited.add((x,y))
        
        
        while q:
            
            top = q.pop(0)
            cost = top[0]
            #print(top)
            xs = top[1]
            ys = top[2]
            
            if grid[xs][ys] == 0:
                newg[xs][ys] = cost
            
            for neix,neiy in ((xs+1,ys),(xs-1,ys),(xs,ys+1),(xs,ys-1)):
                
                if 0<=neix<len(grid) and 0<=neiy<len(grid[0]) and (neix,neiy) not in visited:
                    q.append((cost+1, neix,neiy))
                    visited.add((neix,neiy))
                    
                    
        result = -1
        
        for x in range(len(newg)):
            
            result = max(result, max(newg[x]))
            
        return result if result > 0 else -1
