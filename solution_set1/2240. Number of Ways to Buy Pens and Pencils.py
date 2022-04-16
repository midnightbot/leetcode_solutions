##ss
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        ways  = 0
        
        maxp = total // cost1
        
        for x in range(maxp + 1):
            left = total - (x*cost1)
            ways+= left//cost2 + 1
            
        return ways
            
