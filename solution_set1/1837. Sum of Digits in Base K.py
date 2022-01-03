##ss
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        #strs = ""
        c = 1
        ans = 0
        while n > 0:
            #strs += str(n%k)
            ans+=n%k
            n //= k
            
        return ans
            
        
            
            
        
