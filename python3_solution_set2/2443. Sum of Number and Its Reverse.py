class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        
        for x in range(0,num+1):
            if x + int(str(x)[::-1]) == num:
                return True
            
        return False
        
