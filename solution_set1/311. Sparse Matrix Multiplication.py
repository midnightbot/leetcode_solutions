##ss
import numpy as np
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        mat1 = np.array(mat1)
        mat2 = np.array(mat2)
        
        ans = matmul(mat1, mat2)
        
        return ans.tolist()
        
