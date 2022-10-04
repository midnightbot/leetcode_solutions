##ss
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        
        ## allocate 'k' mailboxes
        
        houses = sorted(houses)
        
        if k >= len(houses):
            return 0
        
        ## basically find 'k' clusters, then place a cluster for each mailbox at median
        
        #print(median(houses))
        
        def find_median(pos1,pos2):
            return int(median(houses[pos1:pos2+1]))
        
        def find_cost(pos1,pos2,meds):
            
            return sum([abs(houses[x]-meds) for x in range(pos1,pos2+1)])
            
        @lru_cache(None)
        def can_do(l,k):
            #print(l,k)
            if k == 0:
                if l == len(houses):
                    return 0
                else:
                    return float('inf')
            elif k > 0 and l < len(houses):
                ans = float('inf')
                for nei in range(l,len(houses)):
                    meds = find_median(l,nei)
                    ans = min(ans, find_cost(l,nei,meds) + can_do(nei+1,k-1))
                
                return ans
            
            return float('inf') ## all other cases where all 'k' mailboxes not used or some houses not in any cluster, return inf as this is not the optimal answer in any case
            
                
        return can_do(0,k)
            
        
