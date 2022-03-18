##ss
import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        ##distancetolastnode implemented by dijkstras from n to all other nodes
        ## [a,b,c,d] - > dtol(a) > dtol(b) > dtol(c) > dtol(d)
        
        ## dp + dijkstras
        
        ans = [float('inf') for x in range(n+1)]
        ans[0] = "no_value"
        graph = {}
        modulo = 10**9 + 7
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
            heapq.heappush(q,[0,start])
            
            ans[start] = 0
            visited = set()
            
            while q:
                top = heapq.heappop(q)
                
                dist = top[0]
                node = top[1]
                
                if node not in visited:
                    visited.add(node)
                    
                    if node in graph:
                        for z in graph[node]:
                            if ans[z[0]] > dist + z[1]:
                                ans[z[0]] = dist + z[1]
                                heapq.heappush(q,[ans[z[0]],z[0]])
                                
                                
            
        dijkstra(n)
        #print(ans)
        
        ##paths from 1->n such that dtol condition is maintained
        @lru_cache(None)
        def thisways(node):
            
            if node == n:
                return 1
            
            else:
                temp = 0
                for z in graph[node]:
                    if ans[z[0]] < ans[node]:
                        temp += thisways(z[0])
                        temp = temp % modulo
                        
                return temp%modulo
            
        return thisways(1)%modulo
