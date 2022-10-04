class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==0:
            return False
        
        if n<0:
            return False
        
        while n!=1:
            if n%81 ==0:
                n=n/81
                
            elif n%27==0:
                n=n/27
                
            elif n%9==0:
                n=n/9
                
            elif n%3==0:
                n=n/3
                
            elif n%3!=0:
                return False
            
        
        if n==1:
            return True
        
