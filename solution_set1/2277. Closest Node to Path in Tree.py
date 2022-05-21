##ss
class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        graph = {x:[] for x in range(n)}
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        #print(graph)
        
        
        ## get nodes on that path
        ## dist of each node from the mentioned node in the query
        
        def find_nodes(start,end): ## get nodes on that path
            
            if start == end:
                return str(start)
            
            q = [[start,str(start)]]
            visited = set()
            
            while q:
                top,path = q.pop(0)
                for nei in graph[top]:
                    if nei not in visited:
                        q.append([nei,path+ ","+ str(nei)])
                        if nei == end:
                            return path + "," + str(nei)
                        visited.add(nei)
        
        
        @lru_cache(None)
        def do_bfs(querynode):
            
            dist = [float('inf') for x in range(n)]
            dist[querynode] = 0
            
            q = [[querynode,0]]
            visited = set()
            visited.add(querynode)
            
            while q:
                top,lens = q.pop(0)
                
                for nei in graph[top]:
                    if nei not in visited:
                        dist[nei] = lens + 1
                        visited.add(nei)
                        q.append([nei,lens+1])
                        
                        
            return dist
            
            
        result = []
            
        for startnode,endnode, querynode in query:
            
            paths = find_nodes(startnode, endnode)
            
            distances = do_bfs(querynode)
            
            #print(paths)
            if paths == "" or paths is None:
                result.append(0)
            
            else:
                comp = paths.split(",")
                #print(comp)
                ans = float('inf')
                node = -1
                for nds in comp:
                    if distances[int(nds)] < ans:
                        ans = distances[int(nds)]
                        node = nds
                    #ans = min(ans, distances[int(nds)])

                result.append(node)
            
        return result
