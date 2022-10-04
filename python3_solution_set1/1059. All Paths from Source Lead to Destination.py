##ss
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {}
        
        for x in range(len(edges)):
            if edges[x][0] in graph:
                graph[edges[x][0]].append(edges[x][1])
                
            else:
                graph[edges[x][0]] = [edges[x][1]]
                
        if destination in graph:
            return False
        
        visited = set()
        def expand(node):
            
            if node not in graph:
                return node == destination
            
            for nei in graph[node]:
                if nei in visited:
                    return False
                visited.add(nei)
                if not expand(nei):
                    return False
                
                visited.remove(nei)
                
            return True
        
        return expand(source)
                
