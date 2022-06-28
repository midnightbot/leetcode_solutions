import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        
        mods = 10**9+7
        c = 0
        
        for x in range(1,n+1):
            if x in prime:
                c+=1
        
        return (math.factorial(c) * math.factorial(n-c))%mods
        
        
        
