##ss
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        for x in range(num//2+2):
            if x*x == num:
                return True
            
            if x*x > num:
                break
                
        return False
        
