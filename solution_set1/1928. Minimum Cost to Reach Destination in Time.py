##fully ss
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        ## go from 0 to n-1
        ## simple recursion. 
        ## dp[node,time] = minimum-cost to reach node from last-node in 'time' time
        graph = {}
        for x in range(len(edges)):
            if edges[x][0] in graph:
                graph[edges[x][0]].append([edges[x][1],edges[x][2]])
            else:
                graph[edges[x][0]] = [[edges[x][1], edges[x][2]]]
                
            if edges[x][1] in graph:
                graph[edges[x][1]].append([edges[x][0],edges[x][2]])
                
            else:
                graph[edges[x][1]] = [[edges[x][0],edges[x][2]]]
                
                
        dp = [float('inf') for x in range(len(passingFees))]
        
        @lru_cache(None)
        def find_path(node,time):
            if node == 0:
                if time <= maxTime:
                    return passingFees[0]
                else:
                    return float('inf')
                
            elif node < 0 or time > maxTime:
                return float('inf')
            
            else:
                thisans = float('inf')
                for nei,travel_time in graph[node]:
                    thisans = min(passingFees[node] + find_path(nei,time+travel_time), thisans)
                    
                return thisans
        ans = find_path(len(passingFees)-1,0)
        return ans if ans!=float('inf') else -1
            
