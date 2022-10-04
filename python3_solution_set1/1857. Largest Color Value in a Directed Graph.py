##ss
## 37 mins

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        ##brute-force -> ans = max(find all paths, find max color of each path)
        
        ##detect for cycles -> by union find or topo-sort (initial step)
        
        ## dp[node][color] = color of nodes in path starting from node with color = 'color'
        
        #s = [0 for x in range(10**6)]
        
        #print("done")
        ## can allocate 10**6 space, so normal 2-D dp
        
        clrs = set()
        for x in colors:
            clrs.add(x)
            
        #dp = [[0 for x in range(len(clrs))] for y in range(len(colors))] -> used lru_cache
        ans = 1
        
        graph = {x:[] for x in range(len(colors))}
        
        for x in range(len(edges)):
            graph[edges[x][0]].append(edges[x][1])
            
        #print(graph)
        #self.print_dp(dp)
        
        #c_map = {list(clrs)[x]:x for x in range(len(list(clrs)))}
        ## start from node with 0 indegree, as this will contain all paths with maximum lengths
        
        @lru_cache(None)
        def solve_dp(node,color):

            if len(graph[node])!=0:
                thisans = 0
                for nei in graph[node]:
                    if colors[nei] == color:
                        thisans = max(thisans, 1 + solve_dp(nei,color))
                        
                    else:
                        thisans = max(thisans, solve_dp(nei,color))
                 
                return thisans
            else:
                return 0
                
        def find_topo():
            
            visited = set()
            indegree = {x:0 for x in range(len(colors))}
            ini = []
            for x in range(len(edges)):
                indegree[edges[x][1]]+=1
                
            q = []
            for x in indegree:
                if indegree[x] == 0:
                    q.append(x)
                    ini.append(x)
                    
            while q:
                node = q.pop(0)
                
                if node not in visited:
                    visited.add(node)
                    
                    for nei in graph[node]:
                        indegree[nei]-=1
                        
                        if indegree[nei] == 0:
                            q.append(nei)
            
            
            return ini, visited
        a,b = find_topo()
        
        if len(b) < len(colors):
            return -1
        
        ## finding the result
        
        result = 0
        
        #print(solve_dp(0,'a'))
        #print(a)
        for x in range(len(a)):
            for y in clrs:
                if colors[a[x]] == y:
                    result = max(result, 1+ solve_dp(a[x],y))
                else:
                    result = max(result, solve_dp(a[x],y))
                #print(a[x],y,result,colors[x])
        return result
    
    ##pdf explanation : https://github.com/midnightbot/leetcode_solutions/blob/main/solution_set1/1857.%20Largest%20Color%20Value%20in%20a%20Directed%20Graph.pdf
