##ss
##simple bfs/dfs with heaps
import heapq
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        q = [(-grid[0][0],0,0)]
        
        visited = set()
        visited.add((0,0))
        while q:
            #print(q)
            top = heapq.heappop(q)
            cost = top[0]
            xs = top[1]
            ys = top[2]
            
            if [xs,ys] == [len(grid)-1,len(grid[0])-1]:
                return -cost
            
            
            for nex,ney in ((xs+1,ys),(xs-1,ys),(xs,ys+1),(xs,ys-1)):
                if 0<=nex<len(grid) and 0<=ney<len(grid[0]) and (nex,ney) not in visited:
                    newcost = max(cost, -grid[nex][ney])

                    visited.add((nex,ney))
                    heapq.heappush(q,(newcost,nex,ney))
        
