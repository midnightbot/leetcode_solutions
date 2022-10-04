##ss
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        ##simple count island problem
        ##just while counting islands of grid2, check if corresponding point of that island in grid1 are all 1
        
        ans = 0
        
        for x in range(len(grid2)):
            for y in range(len(grid2[0])):
                if grid2[x][y] == 1 and grid1[x][y] == 1:
                    ans+=self.expand(grid1,grid2,x,y)
                    #print(x,y,grid2)
                    
        return ans
                    
                    
    
    def expand(self,grid1,grid2,x,y):
        
        queue = set()
        queue.add(tuple((x,y)))
        points = set() ##contains all points of this new island in grid2
        while queue:
            temp = set()
            for x in range(len(queue)):
                node = queue.pop()
                row = node[0]
                col = node[1]
                points.add(tuple((row,col)))
                if row-1>=0 and grid2[row-1][col] == 1:
                    temp.add(tuple((row-1,col)))
                    
                    
                if row + 1 < len(grid2) and grid2[row+1][col] == 1:
                    temp.add(tuple((row+1,col)))
                    
                if col - 1>=0 and grid2[row][col-1] == 1:
                    temp.add(tuple((row,col-1)))
                    
                if col + 1 < len(grid2[0]) and grid2[row][col+1] == 1:
                    temp.add(tuple((row,col+1)))
                    
                    
                grid2[row][col] = 0
                
            queue = temp
            temp = set()
                
                
        points = list(points)
        for x in range(len(points)): ##check if all poins of this island are also 1 in grid1
            if grid1[points[x][0]][points[x][1]]!=1:
                return 0
            
        return 1
        
