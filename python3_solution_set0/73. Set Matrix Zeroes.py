##ss
##Space complexity O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #self.printmat(matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    self.setrowcol(x,y,matrix)
                    
        self.makeans(matrix)
        #print("____")
        #self.printmat(matrix)
                
    
    def setrowcol(self,row,col,matrix):
        
        for x in range(len(matrix[0])):
            if matrix[row][x]!=0:
                matrix[row][x] = "c"
            
            
        for x in range(len(matrix)):
            if matrix[x][col]!=0:
                matrix[x][col] = "c"
            
    
    def makeans(self,matrix):
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == "c":
                    matrix[x][y] = 0
                    
                    
    def printmat(self,matrix):
        for x in range(len(matrix)):
            print(matrix[x])
        
        
