###ss
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        ## simple
        ## n times dijkstras
        
        graph = {}
        
        for x in range(len(edges)):
            if edges[x][0] in graph:
                graph[edges[x][0]].append([edges[x][1],edges[x][2]])
                
            else:
                graph[edges[x][0]] = [[edges[x][1],edges[x][2]]]
                
            if edges[x][1] in graph:
                graph[edges[x][1]].append([edges[x][0],edges[x][2]])
                
            else:
                graph[edges[x][1]] = [[edges[x][0],edges[x][2]]]
                
                
        def dijkstra(start):
            q = []
            ans = [float('inf') for x in range(n)]
            heapq.heappush(q,[0,start])
            visited = set()
            ans[start] = 0
            while q:
                top = heapq.heappop(q)
                
                node = top[1]
                dist = top[0]
                
                if node not in visited:
                    visited.add(node)
                    
                    if node in graph:
                        for z in graph[node]:
                            if ans[z[0]] > dist + z[1]:
                                ans[z[0]] = dist + z[1]
                                heapq.heappush(q,[ans[z[0]], z[0]])
                            
                            
            return ans
        
        
        
        fulls = []
        
        for x in range(n):
            fulls.append(dijkstra(x))
            
        count = []
        
        for x in range(len(fulls)):
            c = 0
            for y in range(len(fulls[x])):
                if fulls[x][y] <= distanceThreshold:
                    c+=1
                    
            count.append(c-1)
            
        mins = float('inf')
        indx = -1
        
        for x in range(len(count)):
            
            if mins > count[x]:
                mins = count[x]
                indx = x
                
            elif mins == count[x]:
                indx = x
                
        return indx
                
                    
                    
        
