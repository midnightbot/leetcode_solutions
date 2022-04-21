##ss
import heapq
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        ## just maitain heap of which river is to be dried nexxt
        next_dry = []
        pos = {}
        ans = []
        def add_next_lake(indx):
            
            l = rains[indx]
            if len(pos[l]) == 0:
                pos.pop(l)
                
            else:
                diff = pos[l][0] - indx
                heapq.heappush(next_dry, [diff, l])
                
            
        for indx,val in enumerate(rains):
            if val in pos:
                pos[val].append(indx)
                
            else:
                pos[val] = [indx]
                
        full = set()
        
        for indx,lake in enumerate(rains):
            if lake in full:##base case no answer found
                return []
            
            elif lake!=0 and lake not in full:
                full.add(lake)
                pos[lake] = pos[lake][1:]
                add_next_lake(indx)
                ans.append(-1)
                
            elif lake == 0:
                
                if next_dry:
                    dist,drying_lake = heapq.heappop(next_dry)
                    full.remove(drying_lake)
                    ans.append(drying_lake)
                    
                else:
                    ans.append(1)
            
        return ans
