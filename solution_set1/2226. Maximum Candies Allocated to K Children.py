##ss
import heapq
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        candies = sorted(candies,reverse = True)
        
        l = 0
        r =  (sum(candies) // k)
        def can_done(c):
            st = 0
            
            for x in candies:
                st+=x//c
                
            #print(c, st)
            return st
            
        while l < r:
            mid = (l+r+1)//2
            #print(l,r)
            if can_done(mid) < k:
                r = mid - 1
                
            else:
                l = mid
                
        return l
            
            
            
        
