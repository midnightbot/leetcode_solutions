##ss
class Solution:
    def isHappy(self, n: int) -> bool:
        
        count = 0
        while n!=1 and count <=10:
            n = sum([int(x)**2 for x in str(n)])
            count+=1
            
        
        if n == 1:
            return True
        else:
            return False
            
