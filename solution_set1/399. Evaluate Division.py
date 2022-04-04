##ss
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        ## simple bfs
        nodes = set()
        for x,y in equations:
            nodes.add(x)
            nodes.add(y)
            
        g = {x:[] for x in nodes}
        
        for c,(x,y) in enumerate(equations):
            g[x].append([y,values[c]])
            g[y].append([x,1/values[c]])
            
        ans = [float(-1) for x in range(len(queries))]
        ## now for queries just find path from c-> d and keep on multiplying the values
        def do_bfs(c,d):
            q = [(c,1)]
            visited = set()
            visited.add(c)
            if c not in g:
                return float(-1)
            while q:
                top = q.pop(0)
                node = top[0]
                val = top[1]
                if node == d:
                    return val
                
                else:
                    for nei,cost in g[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append((nei,val *cost))
                            
            return float(-1)

            
        for i, (c,d) in enumerate(queries):
            ans[i] = do_bfs(c,d)
        
        return ans
