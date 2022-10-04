#ss
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        ## if n = 1 (5)
        ##if n = 2 (5*4)
        ## if n = 5 (5*4*5*4*5)  i.e (20*20*5)  
        return (pow(20,n//2,pow(10,9)+7)*pow(5,n%2,pow(10,9)+7)) % (pow(10,9)+7)
