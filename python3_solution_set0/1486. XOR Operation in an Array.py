class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        kk = start
        for x in range(1,n):
            kk^=(start + 2*x)
            
        return kk
            
