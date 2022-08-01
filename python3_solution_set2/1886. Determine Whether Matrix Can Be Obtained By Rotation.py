##ss
import numpy
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        temp = numpy.array(mat)
        if temp.tolist() == target:
            return True
        temp = numpy.rot90(temp)
        if temp.tolist() == target:
            return True
        temp = numpy.rot90(temp)
        if temp.tolist() == target:
            return True
        temp = numpy.rot90(temp)
        if temp.tolist() == target:
            return True
        return False
