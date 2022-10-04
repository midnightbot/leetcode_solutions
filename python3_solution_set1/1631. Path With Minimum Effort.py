##ss
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ## to go from 0,0 to m-1,n-1
        ##up,down,left,right is allowed moves
        ##effort = max(abs(pt1-pt2)) where pt1,pt2 are consecutive points on the path
        
        graph = {}
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def isvalid(x,y):
            
            return 0<=x<len(heights) and 0<=y < len(heights[0])
            
        def makenode(x,y):
            return str(x) + "," + str(y)
        
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                
                
                for z in moves:
                    if isvalid(z[0]+x, z[1] + y):
                        if makenode(x,y) in graph:
                            graph[makenode(x,y)].append([makenode(z[0]+x, z[1]+y), abs(heights[x][y] - heights[z[0]+x][z[1]+y])])
                            
                        else:
                            graph[makenode(x,y)] = [[makenode(z[0]+x, z[1]+y), abs(heights[x][y] - heights[z[0]+x][z[1]+y])]]
                            
        ##now that we have graph, we can use dijkstras
        ##instead of addding path lengths, keep track of max edge cost
        
        ans = {str(x)+","+str(y): float('inf') for x in range(len(heights)) for y in range(len(heights[0]))}
                
        q = [[0,"0,0"]]
        ##cost, node
        ans["0,0"] = 0
        visited = set()
        while q:
            #print(q)
            top = heapq.heappop(q)
            #print(top)
            node = top[1]
            cost = top[0]
            if node not in visited:
                visited.add(node)
                ans[node] = min(ans[node],cost)
                if node in graph:
                    for z in graph[node]:
                        
                        if ans[z[0]] > max(z[1],ans[node]):
                            ans[z[0]] = max(z[1],ans[node])
                            heapq.heappush(q, [ans[z[0]], z[0]])
                            #print(z[0], ans[z[0]],node)   
        return ans[makenode(len(heights)-1, len(heights[0])-1)]
                            
                            
    
                
