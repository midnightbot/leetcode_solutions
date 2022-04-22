##ss
import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        ## div(a) + div(b) + div(c) - (diva*b) - div(b*c) - div(a*c) + div(a*b*c)
        def count(n):
            ab = a*b//gcd(a,b)
            ac = a*c //gcd(a,c)
            bc = b*c//gcd(b,c)
            
            abc = a*bc//gcd(a,bc)
            
            return n//a+n//b+n//c-n//ab-n//ac-n//bc+n//abc
        
        
        i = 1
        j = min(a,b,c) * n
        
        while i < j:
            mid = i + (j-i)//2
            
            if count(mid) >= n:
                j = mid 
            else:
                i = mid + 1
                
        return i
        
        
