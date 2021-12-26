##ss
import numpy as np

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        
        ans = []
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    temp,temp2 = self.getisland(grid,x,y)
                    t1 = temp[::-1]
                    t2 = temp2[::-1]
                    #print(temp,t1)
                    #print(temp2,t2)
                    #print("old",ans)
                    #print("****")
                    #print("inside")
                    if temp in ans or t1 in ans or temp2 in ans or t2 in ans or np.array(t1).T.tolist() in ans or np.array(t2).T.tolist() in ans or np.array(temp).T.tolist() in ans or np.array(temp2).T.tolist() in ans or np.array(t1).T.tolist()[::-1] in ans or np.array(t2).T.tolist()[::-1] in ans or np.array(temp).T.tolist()[::-1] in ans or np.array(temp2).T.tolist()[::-1] in ans:
              
                        #ans.append(temp)
                        ans = ans
                        
                    else:
                        ans.append(temp)
                        
                    #print("new",ans)
                    #print("***")
          
        #print(ans)
        return len(ans)
                    
                    
          
    def check(self,arr1,ans):
        
        for x in range(len(ans)):
            if ans[x] == arr1:
                return True
            
        return False
    
    def getisland(self,grid,x,y):
        ans = []
        queue = set()
        queue.add(tuple((x,y)))
        visited = set()
        while queue:
            
            for x in range(len(queue)):
                node = queue.pop()
                visited.add(tuple((node)))
                if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                    queue.add(tuple((node[0]+1,node[1])))
                    
                    
                if node[0] - 1>=0 and grid[node[0]-1][node[1]] == 1:
                    queue.add(tuple((node[0]-1,node[1])))
                    #queue.append((node[0]-1,node[1]))
                    
                    
                if node[1]-1>=0 and grid[node[0]][node[1]-1] == 1:
                    queue.add(tuple((node[0],node[1]-1)))
                    #queue.append((node[0],node[1]-1))

                    
                if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                    queue.add(tuple((node[0],node[1]+1)))
                    #queue.append((node[0],node[1]+1))
                    
                    
                grid[node[0]][node[1]] = 0
         
        shape1,shape2  = self.makeshape(visited)
        return shape1,shape2
    
    def makeshape(self,visited):
        xmin = float('inf')
        ymin = float('inf')
        xmax = 0
        ymax = 0
        visited = list(visited)
        for x in range(len((visited))):
            xmin = min(xmin,visited[x][0])
            ymin = min(ymin, visited[x][1])
            
            xmax = max(xmax,visited[x][0])
            ymax = max(ymax,visited[x][1])
            
            
        ans = [[0 for x in range(ymax-ymin+1)] for y in range(xmax-xmin+1)]
        #print(len(ans),len(ans[0]))
        for x in range(len(visited)):
            ans[visited[x][0]-xmin][visited[x][1]-ymin] = 1
           
        mats = np.array(ans)
        return ans,(mats.T).tolist()
            
        
