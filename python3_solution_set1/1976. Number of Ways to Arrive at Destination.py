##ss
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        modulo = 10**9 + 7
        
        
        ans = [float('inf') for x in range(n)]
        ans[0] = 0
        
        graph = {}
        q = []
        for x in range(len(roads)):
            
            if roads[x][0] in graph:
                graph[roads[x][0]].append([roads[x][1],roads[x][2]])
                
            else:
                graph[roads[x][0]] = [[roads[x][1],roads[x][2]]]
            
            
            if roads[x][1] in graph:
                graph[roads[x][1]].append([roads[x][0],roads[x][2]])
                
            else:
                graph[roads[x][1]] = [[roads[x][0],roads[x][2]]]
                
        heapq.heappush(q,[0,0])
        ##dist,node
        
        visited = set()
        
        while q:
            node = heapq.heappop(q)
            
            if node[1] not in visited:
                visited.add(node[1])
                if node[1] in graph:
                    for z in graph[node[1]]:
                        if ans[z[0]] > ans[node[1]] + z[1]:
                            ans[z[0]] = ans[node[1]] + z[1]
                            heapq.heappush(q,[ans[z[0]],z[0]])
                            
        #print(ans)
        time = ans[-1]
        ##we have to reach last node in 'time'
        
        @lru_cache(None)
        def find_ways(city):
            #print(city)
            if city == 0:
                return 1
            
            else:
                cnt = 0
                if city in graph:
                    for z in graph[city]:
                        if ans[z[0]] + z[1] == ans[city]:
                            cnt+=find_ways(z[0])
                            
                return cnt%modulo
            
            
        return find_ways(n-1)%modulo
        
