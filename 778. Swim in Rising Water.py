##ss
##Solution 1 (Time Limit Exceeded)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        
        ##just find paths and max of the path will be the time 
        ##return the path with min max time
        ##using bfs/dfs
        ans = []
        mins = []
        mins.append(float('inf'))
        self.expand(grid,0,0,ans,grid[0][0],[],mins)
        return min(ans)
        
    def expand(self,grid,x,y,ans,time,visited,mins):
        #print(x,y,visited,mins)
        
        if x == len(grid)-1 and y == len(grid[0])-1:
            #print("inisde")
            mins[0] = min(mins[0], time)
            ans.append(time)
            
            
        if x-1 >=0 and (x-1,y) not in visited and grid[x-1][y] < mins[0] and time < mins[0]:
            l = copy.deepcopy(visited)
            l.append((x-1,y))
            temp1 = max(time,grid[x-1][y])
            self.expand(grid,x-1,y,ans,temp1,l,mins)
            
            
        if x+1 < len(grid) and (x+1,y) not in visited and grid[x+1][y] < mins[0] and time < mins[0]:
            l = copy.deepcopy(visited)
            l.append((x+1,y))
            temp2 = max(time,grid[x+1][y])
            self.expand(grid,x+1,y,ans,temp2,l,mins)
            
            
        if y-1 >=0 and (x,y-1) not in visited and grid[x][y-1] < mins[0] and time < mins[0]:
            l = copy.deepcopy(visited)
            l.append((x,y-1))
            temp3 = max(time,grid[x][y-1])
            self.expand(grid,x,y-1,ans,temp3,l,mins)
            
            
        if y + 1 < len(grid[0]) and (x,y+1) not in visited and grid[x][y+1] < mins[0] and time < mins[0]:
            l = copy.copy(visited)
            l.append((x,y+1))
            temp4 = max(time,grid[x][y+1])
            self.expand(grid,x,y+1,ans,temp4,l,mins)
            
        
##Solution 2 (Using A* algorithm, using priority queue) Time Limit Exceeded, but better results than bfs/dfs
##heuristic for A* considered : expanding points that have min time to reach till now
import queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ##bfs/dfs TLE
        ## now will try A* algorithm
        
        frontier = queue.PriorityQueue()
        visited = set()
        
        frontier.put((grid[0][0],(0,0)))
        
        while len(frontier.queue)!=0:
            curr = frontier.get()
            time = curr[0]
            x = curr[1][0]
            y = curr[1][1]
            
            if x == len(grid)-1 and y == len(grid)-1:
                return time
            
            visited.add(tuple((x,y)))
            
            if x-1>=0 and (x-1,y) not in visited:
                frontier.put((max(time,grid[x-1][y]),(x-1,y)))
                
            if x+1 < len(grid) and (x+1,y) not in visited:
                frontier.put((max(time,grid[x+1][y]),(x+1,y)))
                
            if y-1>=0 and (x,y-1) not in visited:
                frontier.put((max(time,grid[x][y-1]),(x,y-1)))
                
            if y+1 < len(grid) and (x,y+1) not in visited:
                frontier.put((max(time,grid[x][y+1]),(x,y+1)))
            
##Solution 3 (Using A* Algorithm, and priority queue)
##heuristic considered : expanding neighbour which have min time (neighbors of all points in visited set)
import queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ##bfs/dfs TLE
        ## now will try A* algorithm
        
        frontier = queue.PriorityQueue()
        visited = set()
        
        frontier.put((grid[0][0],(0,0)))
        ans = 0
        
        while len(frontier.queue)!=0:
            curr = frontier.get()
            time = curr[0]
            x = curr[1][0]
            y = curr[1][1]
            ans = max(ans,time)
            if x == len(grid)-1 and y == len(grid)-1:
                return ans
            
            visited.add(tuple((x,y)))
            
            if x-1>=0 and (x-1,y) not in visited:
                frontier.put((grid[x-1][y],(x-1,y)))
                
            if x+1 < len(grid) and (x+1,y) not in visited:
                frontier.put((grid[x+1][y],(x+1,y)))
                
            if y-1>=0 and (x,y-1) not in visited:
                frontier.put((grid[x][y-1],(x,y-1)))
                
            if y+1 < len(grid) and (x,y+1) not in visited:
                frontier.put((grid[x][y+1],(x,y+1)))
            
##Solution 4 (Using A* Algorithm with heaps)
import queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ##bfs/dfs TLE
        ## now will try A* algorithm
        
        frontier = [(grid[0][0],0,0)]
        visited = {(-1,-1)}
        
        #frontier.append()
        ans = 0
        while len(frontier)!=0:
            time,x,y = heapq.heappop(frontier)
            ans = max(ans,time)
            
            if x == len(grid)-1 and y == len(grid)-1:
                return ans
            
            visited.add((x,y))
            
            if x-1>=0 and (x-1,y) not in visited:
                heapq.heappush(frontier, (grid[x-1][y],x-1,y))
                #frontier.put((max(time,grid[x-1][y]),(x-1,y)))
                
            if x+1 < len(grid) and (x+1,y) not in visited:
                heapq.heappush(frontier, (grid[x+1][y],x+1,y))
                #frontier.put((max(time,grid[x+1][y]),(x+1,y)))
                
            if y-1>=0 and (x,y-1) not in visited:
                heapq.heappush(frontier, (grid[x][y-1],x,y-1))
                #frontier.put((max(time,grid[x][y-1]),(x,y-1))
                
            if y+1 < len(grid) and (x,y+1) not in visited:
                heapq.heappush(frontier, (grid[x][y+1],x,y+1))
                #frontier.put((max(time,grid[x][y+1]),(x,y+1)))
            
