##ss
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ##simple topological sort
        graph = {}
        indegree = {}
        for x in range(numCourses):
            indegree[x] = 0
            
        for x in range(len(prerequisites)):
            if prerequisites[x][1] in graph:
                graph[prerequisites[x][1]].append(prerequisites[x][0])
                
            else:
                graph[prerequisites[x][1]] = [prerequisites[x][0]]
                
            
            indegree[prerequisites[x][0]]+=1
                
            
        #print(graph,indegree)
        queue = []
        visited = set()
        #print(graph,indegree)
        for x in indegree.keys():
            if indegree[x] == 0:
                queue.append(x)
                
        while queue:
            for x in range(len(queue)):
                node = queue.pop(0)
                #print(graph[node],node)
                if node in graph:
                    for nei in graph[node]:
                        #print(nei,"insidd")
                        indegree[nei]-=1
                        if indegree[nei] == 0:
                            queue.append(nei)
                        
                        
                visited.add(node)
                        
        return len(visited) == numCourses
        
