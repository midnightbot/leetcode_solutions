##ss
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        ##simple dijkstras
        
        ans = {x:-float('inf') for x in range(n)}
        
        ans[start] = 0
        graph = {x:[] for x in range(n)}
        
        for x in range(len(edges)):
            graph[edges[x][0]].append([edges[x][1],succProb[x]])
            
            graph[edges[x][1]].append([edges[x][0],succProb[x]])
            
        q = [[-1,start]]
        ##cost, node
        visited = set()
        while q:
            
            top = heapq.heappop(q)
            node = top[1]
            probs = top[0]
            probs = probs * - 1
            if node not in visited:
                visited.add(node)
                
                for z in graph[node]:
                    if probs * z[1] > ans[z[0]]:
                        ans[z[0]] = probs * z[1]
                        heapq.heappush(q,[-ans[z[0]], z[0]])
        #print(ans[end])                
        return ans[end] if ans[end]!=-float('inf') else 0
            
            
