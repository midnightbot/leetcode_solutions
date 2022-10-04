##ss
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visited = {}
        
        for x in range(len(graph)):
            if x not in visited.keys():
                stack = [x]
                visited[x] = 0
                while stack:
                    node = stack.pop()
                    for y in range(len(graph[node])):
                        if graph[node][y] not in visited.keys():
                            stack.append(graph[node][y])
                            visited[graph[node][y]] = visited[node] ^ 1
                            
                        elif visited[graph[node][y]] == visited[node]:
                            return False
                        
        return True
            
        
