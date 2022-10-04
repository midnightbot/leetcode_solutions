##ss
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        c = 0
        
        while target > startValue:
            c+=1
            
            if target%2==0:
                target//=2
                
            else:
                target+=1
                
        return int(c + (startValue - target))
            
            
        
