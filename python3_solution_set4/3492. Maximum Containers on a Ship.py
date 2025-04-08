class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        c = n**2 + 1
        for x in range(c):
            if x*w == maxWeight:
                return x
            
            elif x*w > maxWeight:
                return x-1
        
        if x*w <= maxWeight:
                return x
