##fully ss
##28 mins
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ##only one 0->1 operation is allowed
        
        ##plan : make all islands into groups with a parent
        ##all islands points that are neigh will have same parent
        ##also note the size of the island
        
        ##now check how many diff grps of islands surround any 0
        ##ans will be sum of size of all the islands around this 0 + 1
        ##check for all zero points
        
        ##also at the end just check if without changing any 0 can we get more bigger area, just loop on the self.size and find max
        self.parent = {}
        self.size = {}
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and str(x)+","+str(y) not in self.parent:
                    
                    self.do_bfs(x,y,grid)
                    
        
                    
        ans = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                thisans = 0
                #print(x,y)
                if grid[x][y] == 0:
                    unq = set()
                    if str(x-1)+","+str(y) in self.parent:
                        unq.add(self.parent[str(x-1)+","+str(y)])
                        
                    if str(x+1)+","+str(y) in self.parent:
                        unq.add(self.parent[str(x+1)+","+str(y)])
                        
                    if str(x)+','+str(y-1) in self.parent:
                        unq.add(self.parent[str(x)+','+str(y-1)])
                        
                    if str(x) + ',' + str(y+1) in self.parent:
                        unq.add(self.parent[str(x) + ',' + str(y+1)])
                        
                    
                    for z in list(unq):
                        thisans+=self.size[z]
                ans = max(ans,thisans+1)
         
        for x in self.size:
            ans = max(ans,self.size[x])
            
        return ans
    def do_bfs(self,x,y,grid):
        
        
        par = str(x) + "," + str(y)
        sizes = 0
        q = [[x,y]]
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                sizes+=1
                
                self.parent[str(node[0])+","+str(node[1])] = par
                
                if node[0]-1>=0 and grid[node[0]-1][node[1]] == 1 and str(node[0]-1)+","+str(node[1]) not in self.parent:
                    q.append([node[0]-1,node[1]])
                    self.parent[str(node[0]-1)+","+str(node[1])] = par
                    
                    
                if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1 and str(node[0]+1)+","+str(node[1]) not in self.parent:
                    q.append([node[0]+1,node[1]])
                    self.parent[str(node[0]+1)+","+str(node[1])] = par
                    
                    
                if node[1]-1>=0 and grid[node[0]][node[1]-1] ==1 and str(node[0])+","+str(node[1]-1) not in self.parent:
                    q.append([node[0],node[1]-1])
                    self.parent[str(node[0])+","+str(node[1]-1)] = par
                    
                    
                if node[1]+1< len(grid[0]) and grid[node[0]][node[1]+1] ==1 and str(node[0])+","+str(node[1]+1) not in self.parent:
                    q.append([node[0],node[1]+1])
                    self.parent[str(node[0])+","+str(node[1]+1)] = par
                    
                    
        self.parent[par] = par
        self.size[par] = sizes
            
