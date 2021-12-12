##ss
##simple bfs iteration
##8 branches
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        
        queue = set()
        queue.add(tuple((0,0)))
        
        ## (x,y+1) (x,y-1) (x-1,y-1) (x-1,y) (x-1,y+1) (x+1,y-1) (x+1,y) (x+1,y+1)
        ##x,y (x,y+1) (x+1,y) (x+1,y+1)
        ##x,y  ()
        ans = 0
        while queue:
            temp = set()
            ans+=1
            #print(ans)
            #grid[0][0] = 1
            for x in range(len(queue)):
                node = queue.pop()
                grid[node[0]][node[1]] = 1
                if node[0] == len(grid)-1 and node[1] == len(grid)-1:
                    return ans
                if node[1]+1 < len(grid) and grid[node[0]][node[1]+1] == 0:
                    grid[node[0]][node[1]+1] = 1
                    temp.add(tuple((node[0],node[1]+1)))
                
                if node[1]-1 >=0 and grid[node[0]][node[1]-1] == 0:
                    grid[node[0]][node[1]-1] = 1
                    temp.add(tuple((node[0],node[1]-1)))
                    
                if node[0]-1>=0 and node[1]-1>=0 and grid[node[0]-1][node[1]-1] == 0:
                    grid[node[0]-1][node[1]-1] = 1
                    temp.add(tuple((node[0]-1,node[1]-1)))
                    
                if node[0]-1>=0 and grid[node[0]-1][node[1]] == 0:
                    grid[node[0]-1][node[1]] = 1
                    temp.add(tuple((node[0]-1,node[1])))
                    
                if node[0]-1>=0 and node[1]+1<len(grid) and grid[node[0]-1][node[1]+1] == 0:
                    grid[node[0]-1][node[1]+1] = 1
                    temp.add(tuple((node[0]-1,node[1]+1)))

                if node[0]+1<len(grid) and grid[node[0]+1][node[1]] == 0:
                    grid[node[0]+1][node[1]] = 1
                    temp.add(tuple((node[0]+1,node[1])))
                    
                if node[0]+1 < len(grid) and node[1]-1>=0 and grid[node[0]+1][node[1]-1] == 0:
                    grid[node[0]+1][node[1]-1] = 1
                    temp.add(tuple((node[0]+1,node[1]-1)))
                    
                if node[0]+1 < len(grid) and node[1]+1 < len(grid) and grid[node[0]+1][node[1]+1] == 0:
                    grid[node[0]+1][node[1]+1] = 1
                    temp.add(tuple((node[0]+1,node[1]+1)))
                    
                    
            queue = temp
            temp = set
            
        return -1 
