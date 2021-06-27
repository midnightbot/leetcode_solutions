class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        while n!=1:
            if n%32==0:
                n=n/32
                
            elif n%16==0:
                n=n/16
                
            elif n%8==0:
                n=n/8
                
            elif n%4==0:
                n=n/4
                
            elif n%2==0:
                n=n/2
                
            elif n%2!=0:
                return False
            
            
        if n==1:
            return True
        
