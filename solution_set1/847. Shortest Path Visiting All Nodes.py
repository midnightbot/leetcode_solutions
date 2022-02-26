##Solution1 (Time Limit Exceeded)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        #n = 12, small n indicates just try out all the paths
        
        n = len(graph)
        
        self.ans = float('inf')
        for x in range(len(graph)):
            temp = self.bfs(graph,x)
            
            self.ans = min(self.ans,temp)
            
        return self.ans
        
    def bfs(self,graph,startnode):
        
        q = [[startnode,{},0]]
        
        while q:
            
            for x in range(len(q)):
                temp = q.pop(0)
                node = temp[0]
                visitedc = temp[1]
                visited = copy.deepcopy(visitedc)
                if node in visited:
                    visited[node]+=1
                else:
                    visited[node] = 1
                
                if len(list(visited.keys())) == len(graph):
                    #print(temp)
                    return temp[2]
                
                for z in graph[node]:
                    if z not in visited or visited[z] <= len(graph):
                        
                        if z in visited:
                            visited[z]+=1
                        else:
                            visited[z] = 1
                        #visited[z] = visited.get(z,0)+1
                        #print(visited)
                        
                        q.append([z,visited,temp[2]+1])
                        
                        visited[z]-=1
                        if visited[z] == 0:
                            del visited[z]
                        
        #print("_______")
        return float('inf')
     
        
  ##Solution 2(Accepted)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        anss = float('inf')
        ##use bitmask to represent visited nodes
        
        n = len(graph)
        
        dist = [[float('inf') for x in range(n)]for y in range(n)]
        
        for i,edges in enumerate(graph):
            dist[i][i] = 0
            for edge in edges:
                dist[i][edge] = 1
                
        ##floyd's warshalls
        
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    dist[y][z] = min(dist[y][z], dist[y][x] + dist[x][z])
                    
        @lru_cache(None)            
        def visit(node,visited):
            ##if all nodes visited, say three nodes 111
            ## 111 - 1 = 100
            if visited == (1 << n) - 1:##checking if all nodes are visited
                return 0
            
            ans = float('inf')
            
            for x in range(n):
                
                #if str(visited)[x] == '0':
                if ((1<<x) & (visited)) == 0:##if this node 'x' is not visited, visit it next
                    ans = min(ans, visit(x,(1<<x) | visited) + dist[node][x])
                    
                    
            return ans
        
        #print(dist)
        for x in range(n):
            anss = min(anss, visit(x,(1<<x)))
            
        return anss
                
