##ss
##simple sum in a range question
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        
        for x in range(len(self.matrix)):
            for y in range(1,len(self.matrix[0])):
                self.matrix[x][y]+=self.matrix[x][y-1]
                
        
        

    def update(self, row: int, col: int, val: int) -> None:
        if col!=0:
            diff =   val - (self.matrix[row][col] - self.matrix[row][col-1])
            
        else:
            diff =   val - (self.matrix[row][col] - 0)
        #self.matrix[row][col] = val
        #print(diff)
        for x in range(col, len(self.matrix[0])):
            #print(self.matrix[row][x])
            self.matrix[row][x]+=diff
            
        #print(self.matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans = 0
        #print(self.matrix)
        for x in range(row1,row2+1):
            if col1 == 0:
                ans+=self.matrix[x][col2]
                
            else:
                ans+=self.matrix[x][col2] - self.matrix[x][col1-1]
                
        return ans
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
