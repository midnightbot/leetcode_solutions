##ss
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], label: str) -> List[int]:
        
        maps = {}
        ## just maintain a 26 array for al char freq
        g = {x:[] for x in range(n)} ## making adjaceny graph
        seen = set()
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
        graph = {x:[] for x in range(n)}
        seen.add(0)
        q = [0]
        while q: ### finding the tree connections through bfs traversal
            top = q.pop(0)
            #print(q)
            for nei in g[top]:
                if nei not in seen:
                    seen.add(nei)
                    graph[top].append(nei)
                    q.append(nei)
                
        #print(graph)
        for x in range(len(label)):
            maps[x] = label[x]
            
        #print(maps)
        ans = {x:[0 for y in range(26)] for x in range(n)}
        
        def kadd(a,b):
            #print(a,b)
            return [sum(x) for x in zip(a,b)]
        
        def make_ans(node):## recursive call on children
            if node is None:
                return [0 for x in range(26)]
            
            if node is not None:
                ans[node][ord(maps[node]) - ord('a')]+=1
                if len(graph[node]) >= 1:
                    for nei in graph[node]:
                        ans[node] = kadd(ans[node],make_ans(nei))
                        
                return ans[node]
                
        make_ans(0)
        #print(ans)
        result = [0 for x in range(n)]
        
        for x in range(n):
            result[x] = ans[x][ord(maps[x]) - ord('a')]
            
        return result
