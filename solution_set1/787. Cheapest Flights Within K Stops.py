class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        ##atmost k stops
        ##if there was no limit on stops we would have used dijkstras
        ##now we will have to use dp
        
        
        
        maps = {}
        
        for x in range(len(flights)):
            if flights[x][0] in maps:
                maps[flights[x][0]].append([flights[x][1],flights[x][2]])
                
            else:
                maps[flights[x][0]] = [[flights[x][1],flights[x][2]]]
                
        #ans[src] = 0
        @lru_cache(None)
        def goto(startpoint, k):
            
            if startpoint == dst and k>=0:
                return 0
            
            elif k <=0:
                return float('inf')
                
            else:
                if startpoint in maps:
                    ans = float('inf')
                    for z in maps[startpoint]:
                        ans = min(ans, z[1] + goto(z[0],k-1))
                        
                    return ans
                
                return float('inf')
            
        return -1 if goto(src,k+1) == float('inf') else goto(src,k+1)
