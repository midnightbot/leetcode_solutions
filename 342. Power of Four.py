class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        while n!=1:
            if n%256==0:
                n=n/256
                
            elif n%64==0:
                n=n/64
                
            elif n%16==0:
                n=n/16
                
            elif n%4==0:
                n=n/4
                

                
            elif n%4!=0:
                return False
            
            
        if n==1:
            return True
        
        
