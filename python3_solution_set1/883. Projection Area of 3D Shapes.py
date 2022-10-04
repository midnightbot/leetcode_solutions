import numpy as np
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        xyarea = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]!=0:
                    xyarea+=1
        
        temp = []
        
        for x in range(len(grid)):
            temp.append(max(grid[x]))
            
        yzarea = sum(temp)
        
        
        temp = []
        
        
        grid = np.array(grid).T.tolist()
        
        for x in range(len(grid)):
            temp.append(max(grid[x]))
            
        xzarea = sum(temp)
        
        
        return xyarea + yzarea + xzarea
        
