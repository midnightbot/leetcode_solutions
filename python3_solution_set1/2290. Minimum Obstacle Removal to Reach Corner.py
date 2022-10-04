import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        ##up,down,left,right
        
        n = len(grid)
        m = len(grid[0])
        
        q = []
        dp = [[float('inf') for x in range(m)] for y in range(n)]
        
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        heapq.heappush(q,(grid[0][0],0,0))
        
        while q:
            top_cost,xo,yo = heapq.heappop(q)
            
            if xo == n-1 and yo == m-1:
                return top_cost
            
            for x1,y1 in moves:
                xnew = xo + x1
                ynew = yo + y1
                
                if (xnew>=0 and xnew<n and ynew>=0 and ynew < m) and dp[xnew][ynew] > grid[xnew][ynew] + top_cost:
                    dp[xnew][ynew] = grid[xnew][ynew] + top_cost
                    
                    heapq.heappush(q,(dp[xnew][ynew],xnew,ynew))
        
        
        return -1
