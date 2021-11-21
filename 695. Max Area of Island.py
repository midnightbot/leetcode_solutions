##Solution 1 ss
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        alls = []
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    queue = set()
                    queue.add(tuple((x,y)))
                    c = 0 
                    while queue:
                        c+=1
                        node = queue.pop()
                        grid[node[0]][node[1]] = -1
                        
                        if node[0]+1<len(grid) and grid[node[0]+1][node[1]] == 1:
                            queue.add(tuple((node[0]+1,node[1])))
                            
                        if node[0]-1>=0 and grid[node[0]-1][node[1]] == 1:
                            queue.add(tuple((node[0]-1,node[1])))
                            
                        if node[1]+1<len(grid[0]) and grid[node[0]][node[1]+1]==1:
                            queue.add(tuple((node[0],node[1]+1)))
                            
                        if node[1]-1>=0 and grid[node[0]][node[1]-1] == 1:
                            queue.add(tuple((node[0],node[1]-1)))
                    ans = max(ans,c)
                    
        return ans
        
        
        
        
        
        
        
