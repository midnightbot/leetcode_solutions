##ss
class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        
        rmin = [float('inf') for x in range(n+1)]
        emin = [float('inf') for x in range(n+1)]
        
        ## we start at stop 0 regular
        rmin[0] = 0
        emin[0] = expressCost
        
        for x in range(1,n+1):
            rmin[x] = min(rmin[x-1] + regular[x-1], emin[x-1] + express[x-1] + 0)
            
            emin[x] = min(emin[x-1] + express[x-1], rmin[x-1] + regular[x-1] + expressCost)
        
        return [min(rmin[x],emin[x]) for x in range(1,n+1)]
