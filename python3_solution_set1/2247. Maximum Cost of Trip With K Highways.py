##ss
class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        
        ## exact 'k' highways
        ## visit each city atmost once
        ## return max cost of trips
        ## start at any city
        ## simple dp
        
        graph = {x:[] for x in range(n)}
        
        for x,y,z in highways:
            graph[x].append([y,z])
            graph[y].append([x,z])
            
        #print(graph)
        def conv(strs):
            return [x for x in strs]
        
        def make_strs(arr):
            return "".join(arr)
        
        @lru_cache(None)
        def find_cost(curr, steps, visited):
            if steps == 0:
                return 0
            
            else:
                temp = conv(visited)
                ans = -float('inf')
                for nei,cost in graph[curr]:
                    if temp[nei] == '0':
                        temp[nei] = '1'
                        ans = max(ans, cost + find_cost(nei, steps-1,make_strs(temp)))
                        temp[nei] = '0'
                    
                return ans
            
            
        result = -1
        tempo = ['0' for x in range(n)]
        for x in range(n):
            tempo[x] = '1'
            result = max(result, find_cost(x,k,make_strs(tempo)))
            tempo[x] = '0'
            
        return result
            
        
        
