##ss
##Solution 1
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        for x in range(len(self.matrix)):
            ans = 0
            for y in range(len(self.matrix[0])):
                ans+=self.matrix[x][y]
                self.matrix[x][y] = ans
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if col1 == 0:
            ans = 0
            for x in range(row1,row2+1):
                ans+= self.matrix[x][col2]
        
        else:
            ans = 0
            for x in range(row1,row2+1):
                ans+=self.matrix[x][col2] - self.matrix[x][col1-1]
                
        return ans
                
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
