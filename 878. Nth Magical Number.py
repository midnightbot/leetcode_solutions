##involves number theory logic
##else just simple binary search
import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        
        ## number of numbers divisible by a till m is m//a
        ## number of numbers divisible by b till m is m//b
        ##number of numbers divisible by both a&b till m  is m//lcm(a,b)
 
        lcm = a*b/math.gcd(a,b)
        
        left = 0
        right =  n * min(a,b)
        
        while left < right:
            
            mid = left + (right - left)//2
            #print(mid)
            #print(mid)
           
            
            if n > (mid//a + mid//b - mid//lcm):
                left = mid + 1
                
            else:
                right = mid
                
        return left%(pow(10,9)+7)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
