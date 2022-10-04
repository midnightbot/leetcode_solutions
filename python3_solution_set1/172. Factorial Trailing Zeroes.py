##ss
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ##pow(10) + min(pow(2),pow(5))
        #print(math.factorial(10))
        #print(self.find_pow10(n),self.find_pow2(n),self.find_pow5(n))
        return self.find_pow10(n)+min(self.find_pow2(n),self.find_pow5(n))
    
    def find_pow2(self,n):
        
        ans = 0
        curr = 0
        if n <2:
            return 0
        if n == 2:
            return 1
        
        else:
            curr = 1
            ans = 1
            for x in range(3,n+1):
                if x%2==0:
                    curr = 0
                    temp = x
                    while temp%10==0:
                        temp = temp / 10
                        
                    while temp%2==0:
                        curr+=1
                        temp = temp / 2
                        
                    ans+=curr
                
            return ans
        
    def find_pow5(self,n):
        
        ans = 0
        curr = 0
        if n <5:
            return 0
        if n == 5:
            return 1
        
        else:
            curr = 1
            ans = 1
            for x in range(6,n+1):
                if x%5==0:
                    curr = 0
                    temp = x
                    while temp%10==0:
                        temp = temp / 10
                        
                    while temp%5==0:
                        curr+=1
                        temp = temp / 5
                    
                    ans+=curr
                
            return ans
        
        
    def find_pow10(self,n):
        
        ans = 0
        curr = 0
        if n <10:
            return 0
        if n == 10:
            return 1
        
        else:
            curr = 1
            ans = 1
            for x in range(11,n+1):
                if x%10==0:
                    temp = x
                    curr = 0
                    while temp%10==0:
                        curr+=1
                        temp = temp / 10
                    
                    ans+=curr
                
            return ans
        
        
        
