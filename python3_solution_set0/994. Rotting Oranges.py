#SS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = set()
        ans = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.add(tuple((x,y)))
                    ans[x][y] = 2
                    
                elif grid[x][y] == 1:
                    ans[x][y] = 2
        
        if grid == ans:
            return 0
        #print(queue)
        #print(ans)
        c = -1
        while queue:
            
            #print(queue)
            temp  = set()
            k = 0
            for x in range(len(queue)):
                node = queue.pop()
                grid[node[0]][node[1]] = 2
                if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                    
                    temp.add(tuple((node[0]+1,node[1])))
                    
                if node[0]-1 >= 0 and grid[node[0]-1][node[1]] == 1:
                    
                    temp.add(tuple((node[0]-1,node[1])))
                    
                if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                   
                    temp.add(tuple((node[0],node[1]+1)))
                    
                if node[1]-1>=0 and grid[node[0]][node[1]-1] == 1:

                    temp.add(tuple((node[0],node[1]-1)))
            
            c+=1
            queue |= temp
            #print(grid)
            if grid == ans:
                queue = {}
        
        if grid == ans:
            return c
        else:
            return -1
       
        
          
       
