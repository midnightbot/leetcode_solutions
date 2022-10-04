class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        path_len = 0 ##number of zeros is the path length as all of it has to be covered
        start_x = 0
        start_y = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    path_len+=1
                    
                elif grid[x][y] == 1:
                    start_x = x
                    start_y = y
                    
        #print(path_len,start_x,start_y)
        ans = self.expand(grid,path_len,start_x,start_y)
        return ans
        
        
    def expand(self,grid,path_len,start_x,start_y):
        if (start_x<0 or start_x>=len(grid) or start_y<0 or start_y>=len(grid[0]) or grid[start_x][start_y]==-1):
            return 0
        
        if grid[start_x][start_y] == 2:
            if path_len == -1:
                return 1
            else:
                return 0
            
        grid[start_x][start_y] = -1
        path_len-=1
        
        totalpaths = self.expand(grid,path_len,start_x+1,start_y) + self.expand(grid,path_len,start_x,start_y+1)+ self.expand(grid,path_len,start_x-1,start_y)+self.expand(grid,path_len,start_x,start_y-1)
        
        grid[start_x][start_y] = 0
        path_len+=1
        
        
        return totalpaths
        
        
                    
        
        
        
        
