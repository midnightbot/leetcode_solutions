#ss
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        ## edges that if removed would split the graph into 2 groups
        ##critical edges will not be cycle edges
        ##it would be edges connecting two cycles (connected components)
        
        ##naive solution would be to remove each edge and then do union find, if grps > 1, then it is critical edge
        
        ## good solution would be to use tarjans algorithm
        
        #result = []
        
        time = [0 for x in range(n)]
        low = [0 for x in range(n)]
        
        ##whenevr an edge has nodes of two different low values it is a critical edge
        result = []
        
        graph = {x:[] for x in range(n)}
        
        for x in range(len(connections)):
            graph[connections[x][0]].append(connections[x][1])
            graph[connections[x][1]].append(connections[x][0])
            
        visited = [False for x in range(n)]
        t = {0:0}
        def dfs(visited, curr, parent):
            visited[curr] = True
            time[curr] = low[curr] = t[0]
            t[0]+=1
            
            for nei in graph[curr]:
                if nei == parent:
                    continue
                    
                if not visited[nei]:
                    dfs(visited, nei, curr)
                    low[curr] = min(low[curr], low[nei])
                    
                    if time[curr] < low[nei]:
                        result.append([curr,nei])
                        
                else:
                    low[curr] = min(low[curr], time[nei])
                    
            
        dfs(visited,0,-1)
        
        return result
            
        ##time complexity is O(V+E) -> only one DFS traversal
        
        
        
