##ss
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        ans = []
        for x in range(len(land)):
            for y in range(len(land[0])):
                if land[x][y] == 1:
                    t = self.bfs(land,x,y)
                    ans.append(t)
                    #print(land)
                    
        return ans
        
        
    def bfs(self,land,x,y):
        
        
        thisland = []
        
        q = [(x,y)]
        xs = x
        ys = y
        
        xm = x
        ym = y
        while q:
            node = q.pop(0)
            
            if node[0]-1>=0 and land[node[0]-1][node[1]] == 1:
                q.append((node[0]-1,node[1]))
                land[node[0]-1][node[1]] = -1
                xm = min(xm,node[0]-1)
                
            if node[0]+1 < len(land) and land[node[0]+1][node[1]]==1:
                q.append((node[0]+1,node[1]))
                land[node[0]+1][node[1]] = -1
                xs = max(xs,node[0]+1)
                
            if node[1]-1>=0 and land[node[0]][node[1]-1]==1:
                q.append((node[0],node[1]-1))
                land[node[0]][node[1]-1]=-1
                ym = min(ym,node[1]-1)
                
            if node[1]+1 < len(land[0]) and land[node[0]][node[1]+1]==1:
                q.append((node[0],node[1]+1))
                land[node[0]][node[1]+1] = -1
                ys = max(ys,node[1]+1)
                
                
        return [xm,ym,xs,ys]
                
        
                
                
        
