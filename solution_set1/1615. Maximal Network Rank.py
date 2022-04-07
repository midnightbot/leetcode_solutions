##ss
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        deg = {x:0 for x in range(n)}
        
        for x,y in roads:
            deg[x]+=1
            deg[y]+=1
            
        
        road = set()
        for x,y in roads:
            road.add((x,y))
            road.add((y,x))
            
        maxs = 0
        
        comp = [[x,deg[x]] for x in deg]
        
        for x in range(len(comp)-1):
            for y in range(x+1,len(comp)):
                if (comp[x][0],comp[y][0]) not in road:
                    maxs = max(maxs, comp[x][1] + comp[y][1] )
                    
                else:
                    maxs = max(maxs, comp[x][1] + comp[y][1] - 1)
                
        return maxs
        
        
