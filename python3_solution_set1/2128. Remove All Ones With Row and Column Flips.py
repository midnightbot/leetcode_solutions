##ss
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        ##consider matrix of 0's
        
        ##from this matrix try to make 1st row of mat same as grid
        ##operation1 : row operation of row0
        ##do column operation on positons which need to be zero
        
        ##after this first row of both the matrices are now same
        ##after this check if every row matches the particular grid row or can it be transformed into grid row only be row operations, as column operations are not allowed as it will disrupt the matching of the first row
        
        mat = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        for x in range(len(mat[0])):
            mat[0][x] = 1
            
        for x in range(len(grid[0])):
            if grid[0][x] == 0:
                self.fillcols(mat,x)
                
        #print(mat)
        
        for x in range(1,len(mat)):
            if mat[x] == grid[x] or self.rowoperation(copy.copy(mat[x])) == grid[x]:
                continue
                
            else:
                return False
            
        return True
        
        
        
    def fillcols(self,mat,col):
        
        for x in range(len(mat)):
            mat[x][col] = (mat[x][col] + 1) % 2
            
    def rowoperation(self,ans): ##does 1 change operation on the entire row
        
        for x in range(len(ans)):
            if ans[x] == 1:
                ans[x] = 0
                
            else:
                ans[x] = 1
                
        return ans
        
        
        
