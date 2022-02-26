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
        
