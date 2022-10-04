##ss
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ##dijkstras from 'k' node
        ##find shortest distance from source node to all nodes and then see which is max return that
        ans = [float('inf') for x in range(n+1)]
        
        mapping = {}
        visited = set()
        for x in range(len(times)):
            if times[x][0] in mapping:
                mapping[times[x][0]].append([times[x][1],times[x][2]])
                
            else:
                mapping[times[x][0]] = [[times[x][1],times[x][2]]]
                
        
        q = []
        heapq.heappush(q,[0,k])
        ans[k] = 0
        
        while q:
            node = heapq.heappop(q)
            
            if node[1] not in visited:
                visited.add(node[1])
                
                if node[1] in mapping:
                    #print(mapping[node[1]])
                    for z in mapping[node[1]]:
                        #print(z[0])
                        if ans[z[0]] > ans[node[1]] + z[1]:
                            ans[z[0]] = ans[node[1]] + z[1]
                            heapq.heappush(q,[ans[z[0]],z[0]])
                            
        ans = ans[1:]
        #maxs = -float('inf')
        result = max(ans)
        
        return -1 if result==float('inf') else result
        
