class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        counter = 1
        sums = 0
        
        if n == 1:
            return 1
        
        while sums<n and sums+counter<=n:
            sums+=counter 
            counter+=1
            #print(sums)
            
            
        return counter -1
        
