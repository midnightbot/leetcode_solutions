##ss
import numpy as np
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        comp = [x for x in range(1,len(matrix)+1)]
        comp = set(comp)
        
        for x in range(len(matrix)): ##row check
            thisrow = set(matrix[x])
            if comp!=thisrow:
                return False
            
        
        arr = np.asarray(matrix)
        arr = arr.T
        for x in range(len(arr)): ##column check
            thiscol = set(arr[x])
            if thiscol!=comp:
                return False
            
        return True
