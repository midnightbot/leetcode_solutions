##ss
import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        maxs = 10**7
        t = 0
        for x in range(len(dist) - 1):
            t+= math.ceil(dist[x] / maxs)
            
        t+=dist[-1] / maxs
        
        if t > hour:
            return -1
        
        l = 1
        r = 10**7
        
        def can_do(spd):
            time = 0
            
            for x in range(len(dist) - 1):
                time += math.ceil(dist[x]/spd)
                
                
            time += dist[-1] / spd
            
            return time <= hour
        
        
        while l < r:
            mid = (l+r)//2
            
            if can_do(mid):
                r = mid
                
            else:
                l = mid + 1
                
        return l
        
        
