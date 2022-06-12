class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        ## ss
        ## simple dp, just need to create the graph first
        m = len(grid)
        n = len(grid[0])
        
        graph = {x:[] for x in range(m*n)}
        
        for x in range(len(grid)-1):
            
            for y in range(len(grid[0])):
                
                for nei in grid[x+1]:
                    graph[grid[x][y]].append(nei)
                    
        
        for x in range(len(moveCost)):
            for y in range(len(moveCost[0])):
                if len(graph[x])!=0:
                    graph[x][y] = [graph[x][y], moveCost[x][y]]
                else:
                    continue
                    
        ## min path cost starting from first row and ending in last row
        
        @lru_cache(None)
        def find_ans(node):
            if node in grid[-1]:
                
                return node
            
            else:
                ans = float('inf')
                for nei,cost in graph[node]:
                    ans = min(ans, node + cost + find_ans(nei))
                    
                return ans
            
        return min(find_ans(x) for x in grid[0])
                
                
