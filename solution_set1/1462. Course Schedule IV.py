##ss
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        ##find topo sort
        indegree = {x:0 for x in range(numCourses)}
        graph = {}
        back = [set() for x in range(numCourses)]
                
        for x in range(len(prerequisites)):
            indegree[prerequisites[x][1]]+=1
            
            if prerequisites[x][0] in graph:
                graph[prerequisites[x][0]].append(prerequisites[x][1])
                
            else:
                graph[prerequisites[x][0]] = [prerequisites[x][1]]
                
            back[prerequisites[x][1]].add(prerequisites[x][0])

                
        q = []
        
        
        for x in indegree:
            if indegree[x] == 0:
                q.append(x)
                
        
        while q:
            
            
            top = q.pop(0)

            if top in graph:
                for z in graph[top]:
                    indegree[z]-=1
                    back[z]|=back[top]
                    if indegree[z] == 0:
                        q.append(z)
                                
                                
            
                            
        ans = []
        
    
        for x in range(len(queries)):
            ans.append(queries[x][0] in back[queries[x][1]])
            
        return ans
                
        
        
