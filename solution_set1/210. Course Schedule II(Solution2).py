##ss
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        indegree = {}
        ##simple topological sort
        for x in range(len(prerequisites)):
            if prerequisites[x][1] in graph:
                graph[prerequisites[x][1]].append(prerequisites[x][0])
            else:
                graph[prerequisites[x][1]] = [prerequisites[x][0]]
                
            if prerequisites[x][0] in indegree:
                indegree[prerequisites[x][0]]+=1
            else:
                indegree[prerequisites[x][0]] = 1
                
                
        q = []
        for x in range(numCourses):
            if x not in indegree:
                q.append(x)
                
        ans = []
        visited = set()
        while q:
            
            thisnode = q.pop(0)
            ans.append(thisnode)
            if thisnode in graph:
                for nei in graph[thisnode]:
                    
                    indegree[nei]-=1
                    
                    if indegree[nei] == 0:
                        q.append(nei)
                        visited.add(nei)
                        indegree.pop(nei)
                        
        return ans if len(ans) == numCourses else []
                        
                        
