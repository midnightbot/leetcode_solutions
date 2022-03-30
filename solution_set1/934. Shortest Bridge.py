##ss
##simple bfs
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        ## add points of island1 to get towards island2
        
        def do_bfs(x,y):
            q = [(x,y)]
            visited = set()
            visited.add((0,x,y))
            
            while q:
                top = q.pop(0)
                xs = top[0]
                ys = top[1]
                
                grid[xs][ys] = 0
                for xn,yn in ((xs-1,ys),(xs+1,ys),(xs,ys-1),(xs,ys+1)):
                    if 0<=xn<len(grid) and 0<=yn<len(grid[0]) and grid[xn][yn] == 1 and (0,xn,yn) not in visited:
                        
                        visited.add((0,xn,yn))
                        q.append((xn,yn))
                        
            return visited
        
        def path_bfs(arr):
            q = arr
            seen = set()
            for x in q:
                seen.add((x[1],x[2]))
                
            while q:
                top = q.pop(0)
                cost = top[0]
                xs = top[1]
                ys = top[2]
                
                for xn,yn in ((xs+1,ys),(xs-1,ys),(xs,ys+1),(xs,ys-1)):
                    if 0<=xn<len(grid) and 0<=yn<len(grid[0]) and (xn,yn) not in seen:
                        if grid[xn][yn] == 1:
                            return cost
                        
                        seen.add((xn,yn))
                        q.append((cost+1,xn,yn))
            
        for x in range(len(grid)):
            dec = False
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    cells = do_bfs(x,y)
                    dec = True
                    break
                    
                    
            if dec == True:
                break
        
                    
                    
        return path_bfs(list(cells))       
            
        
