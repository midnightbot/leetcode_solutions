##ss
## 1:30
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        ##always prints rectangles
        ##same color cannot be repeated
        
        ## [0 m*n] -> targetGrid <True or False?>
        
        ## find topo sort on colors, that is order of use of colors
        ## if we get an order to apply colors, such that all colors can be used then target can be formed
        
        
        
        colors = set()
        
        ## counting total colors used
        for x in range(len(targetGrid)):
            for y in range(len(targetGrid[0])):
                colors.add(targetGrid[x][y])
         
        ## 0 is the base color, so remove it
        if 0 in colors:
            colors.remove(0)
            
        ##stores the topleft and bottom right coordinate for each color -> [xl,yl,xr,yr]
        rect = {x:[float('inf'), float('inf'),-1,-1] for x in colors}
        
        for x in range(len(targetGrid)):
            for y in range(len(targetGrid[0])):
                if targetGrid[x][y]!=0:
                    rect[targetGrid[x][y]][0] = min(rect[targetGrid[x][y]][0],x)
                    rect[targetGrid[x][y]][1] = min(rect[targetGrid[x][y]][1],y)
                    rect[targetGrid[x][y]][2] = max(rect[targetGrid[x][y]][2],x)
                    rect[targetGrid[x][y]][3] = max(rect[targetGrid[x][y]][3],y)
                    
           
        #print(rect)
        
        ## now if rect[color1] = [0,0,3,3]
        ## that means we had used printer to print color1 on all cells in range(0,0  -> 3,3)
        ## if at some point between 0,0 -> 3,3 we see it is not color1, it indicates a new rectangle was printed over it overlapping it
        
        ## visualizing it as a graph
        ## say color2, color4 overlap color1
        ## this indicates color1 was done then color2 and color4
        ## color1->color2  color1->color4
        ##similarly find all edges and do topological sort on it
        
        ## if len(topological-sort) = len(colors) -> True
        ## else we cannot print the paper in mentioned target array
        graph = {x:set() for x in colors}
        indegree = {x:0 for x in colors}
        
        
        for x in rect:
            for row in range(rect[x][0], rect[x][2] + 1):
                for col in range(rect[x][1], rect[x][3] + 1):
                    if targetGrid[row][col]!=x:
                        graph[x].add(targetGrid[row][col])
                        
        for x in graph:
            for z in graph[x]:
                indegree[z]+=1
             
        ##doing topological sort on colors
        def topo_sort():
            visited = set()
            topo_order = []
            q = []
            
            for x in indegree:
                if indegree[x] == 0:
                    q.append(x)
                    
            
            
            while q:
                node = q.pop(0)
                
                if node not in visited:
                    visited.add(node)
                    topo_order.append(node)
                    for z in graph[node]:
                        indegree[z]-=1
                        
                        if indegree[z] == 0 and z not in visited:
                            q.append(z)
            return visited
            
            
        ans = topo_sort()
        return len(ans) == len(colors)
