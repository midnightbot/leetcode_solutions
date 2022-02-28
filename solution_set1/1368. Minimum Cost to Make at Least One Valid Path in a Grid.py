##fully ss
from queue import PriorityQueue
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        ##either let the sign be same and move or or change it
        
        ##kind of bfs
        
        ##mark m,n as 0
        ##all points where it can be reached from are also zero, continue so on
        
        ##1-> r, 2->l, 3->d, 4->u
        
        dp = [[float('inf') for x in range(len(grid[0]))] for y in range(len(grid))]
        dp[len(dp)-1][len(dp[0])-1] = 0
        q = []
        heapq.heappush(q,[0,len(dp)-1,len(dp[0])-1])
        visited = set()
        #print(q)
        
        while q:
            #print(dp)
            node = heapq.heappop(q)
            #print(node,q)
            x = node[1]
            y = node[2]
            
            #dp[x][y] = node[0]
            
            
            if self.isvalid(x-1,y,grid) and (dp[x-1][y] > dp[x][y] if self.can_go([x-1,y],[x,y],grid) else 1 + dp[x][y]):
                if self.can_go([x-1,y],[x,y],grid):
                    if dp[x-1][y] > dp[x][y]:
                        heapq.heappush(q,[dp[x][y],x-1,y])
                    dp[x-1][y] = min(dp[x-1][y],dp[x][y])
                    
                    
                else:
                    if dp[x-1][y] > 1 + dp[x][y]:
                        heapq.heappush(q,[1+dp[x][y],x-1,y])
                    dp[x-1][y] = min(dp[x-1][y], 1 + dp[x][y])
                    
                    
                
                
            
            if self.isvalid(x+1,y,grid) and (dp[x+1][y] > dp[x][y] if self.can_go([x+1,y],[x,y],grid) else 1 + dp[x][y]):
                #print("inside")
                if self.can_go([x+1,y],[x,y],grid):
                    if dp[x+1][y] > dp[x][y]:
                        heapq.heappush(q,[dp[x][y],x+1,y])
                        
                    dp[x+1][y] = min(dp[x+1][y], dp[x][y])
                    
                    
                else:
                    if dp[x+1][y] > 1 + dp[x][y]:
                        heapq.heappush(q,[1+dp[x][y],x+1,y])
                        
                    dp[x+1][y] = min(dp[x+1][y], 1 + dp[x][y])
                    
 
            if self.isvalid(x,y-1,grid) and  (dp[x][y-1] > dp[x][y] if self.can_go([x,y-1],[x,y],grid) else 1 + dp[x][y]):
                if self.can_go([x,y-1],[x,y],grid):
                    if dp[x][y-1] > dp[x][y]:
                        heapq.heappush(q,[dp[x][y],x,y-1])
                        
                    dp[x][y-1] = min(dp[x][y-1], dp[x][y])
                    
                    
                else:
                    if dp[x][y-1] > 1 + dp[x][y]:
                        heapq.heappush(q,[1+dp[x][y],x,y-1])
                        
                    dp[x][y-1] = min(dp[x][y-1], 1 + dp[x][y])
                    
                    
                
                    
            if self.isvalid(x,y+1,grid) and (dp[x][y+1] > dp[x][y] if self.can_go([x,y+1],[x,y],grid) else 1 + dp[x][y]) :
                if self.can_go([x,y+1],[x,y],grid):
                    if dp[x][y+1] > dp[x][y]:
                        heapq.heappush(q,[dp[x][y],x,y+1])
                        
                    dp[x][y+1] = min(dp[x][y+1], dp[x][y])
                    
                    
                else:
                    if dp[x][y+1] > 1 + dp[x][y]:
                        heapq.heappush(q,[1+dp[x][y],x,y+1])
                        
                    dp[x][y+1] = min(dp[x][y+1], 1 + dp[x][y])
                    
                    
                
                    
                    
        #self.print_dp(dp)
        return dp[0][0]
    def print_dp(self,dp):
        
        for x in range(len(dp)):
            print(dp[x])
            
    def can_go(self,p1,p2,grid):
        ##i am going from p1-> p2
        #print(p1,p2)
        if p1[1]+1 == p2[1]:
            if grid[p1[0]][p1[1]] == 1:
                return True
            return False
        
        elif p1[1]-1 == p2[1]:
            if grid[p1[0]][p1[1]] == 2:
                return True
            return False
        
        elif p1[0]+1 == p2[0]:
            if grid[p1[0]][p1[1]] == 3:
                return True
            
            return False
        
        elif p1[0]-1 == p2[0]:
            if self.isvalid(p1[0],p1[1],grid) and grid[p1[0]][p1[1]] == 4:
                return True
            return False
        
        
    def isvalid(self,x,y,grid):
        
        return 0<=x< len(grid) and 0<=y < len(grid[0])
