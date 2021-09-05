class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        allPaths = []
        
        def dfs(node, parentPath):
          
            if node == len(graph) - 1:
                allPaths.append(parentPath + [node])
                return 
             
            for adjNode in graph[node]:
                dfs(adjNode, parentPath + [node])
                
        dfs(0, [])

        return allPaths
