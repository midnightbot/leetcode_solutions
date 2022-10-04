##ss
import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #matrix = matrix[::-1]
        arr = np.array(matrix)
        arr = arr.T
        
        return arr.tolist()
        
