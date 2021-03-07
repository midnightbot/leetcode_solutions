class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]<0:
                    count+=1
                    
                    
        return count
