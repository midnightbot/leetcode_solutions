class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_number = -1
        for i in range(len(matrix)):
            if target> matrix[i][0] and target < matrix[i][len(matrix[0]) - 1]:
                row_number = i
                break
            elif target == matrix[i][0]:
                return True
            
            elif target == matrix[i][len(matrix[0]) - 1]:
                return True
            
            
        for j in range(len(matrix[0])):
            if matrix[row_number][j] == target:
                return True
        return False
            

        
