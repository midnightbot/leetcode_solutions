##ss
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        for x in range(len(matrix[0])):
            i = 0
            j = x
            temp = set()
            while i < len(matrix) and j < len(matrix[0]):
                temp.add(matrix[i][j])
                i+=1
                j+=1
                
            if len(temp) >=2:
                return False
            
            
        for x in range(1,len(matrix)):
            i = x
            j = 0
            temp = set()
            while i < len(matrix) and j < len(matrix[0]):
                temp.add(matrix[i][j])
                i+=1
                j+=1
                
                
            if len(temp) >=2:
                return False
            
        return True
                
                
                
        
