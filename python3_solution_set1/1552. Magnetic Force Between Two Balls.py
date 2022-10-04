##ss
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        ## magnetic force is |x-y|
        position = sorted(position)
        l = 0
        r = (position[-1] - position[0]) * 2
        
        def is_good(pos):
            done = 1
            prev = position[0]
            for x in range(1,len(position)):
                if position[x] >= prev + pos:
                    done+=1
                    prev = position[x]
                    
            return done >= m
        
        while l < r:
            #print(l,r)
            mid =  r - (r-l)//2
            
            if is_good(mid):
                l = mid  
                
            else:
                r = mid - 1
                
        return l
        
