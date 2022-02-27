##ss
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        ##[a,b] means a -> b
        
        ##simple bfs
        ##start bfs from node '0' whenever we see a reverse edge add count by 1 
        ans = 0
        
        
        edges = set()
        graph = {}
        for x in range(len(connections)):
            edges.add(tuple(connections[x]))
            
            if connections[x][0] not in graph:
                graph[connections[x][0]] = [connections[x][1]]
            else:
                graph[connections[x][0]].append(connections[x][1])
                
            if connections[x][1] not in graph:
                graph[connections[x][1]] = [connections[x][0]]
            else:
                graph[connections[x][1]].append(connections[x][0])
                
        visited = set()
        
        q = [0]
        
        while q:
            for x in range(len(q)):
                node = q.pop(0)
                
                visited.add(node)
                
                if node in graph:
                    for z in graph[node]:
                        if z not in visited:
                            if tuple([node,z]) in edges:
                                ans+=1
                            visited.add(z)
                            q.append(z)
        
        
        return ans
