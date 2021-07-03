class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0:
            return 0
        for y in range(x+1):
            if y*y == x:
                return y
            elif y*y > x:
                return y-1
        
