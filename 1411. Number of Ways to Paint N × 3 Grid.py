class Solution:
    def numOfWays(self, n: int) -> int:
        
        size2 = 6
        size3 = 6
        mod = pow(10,9)+7
        
        for i in range(1,n):
            temp = size3
            
            size3 = (2*size2 + 2*size3) % mod
            size2 = (3*size2+2*temp)%mod
        
        return (size3+size2)%mod
