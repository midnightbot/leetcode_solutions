##ss
##simple dfs
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        graphs = {x:[] for x in range(len(values))}
        
        for a,b,c in edges:
            graphs[a].append([b,c])
            graphs[b].append([a,c])
            
        #print(graphs)
        
        
        def dfs(node,time,visited):
            
            if node == 0:
                ans = sum([values[x] for x in visited])
                
            else:
                ans = 0
                
            for nei,travel_time in graphs[node]:
                if time >= travel_time:
                    ans = max(ans, dfs(nei, time - travel_time, visited | {nei}))
                    
            return ans
        
        return dfs(0,maxTime,{0})
                
            
            
