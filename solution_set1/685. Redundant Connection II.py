class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        ##tree -> no cycle
        ##rooted tree, hence starting a bfs from the root can cover all the nodes
        
        parent = {}
        conns = {}
        
        def find_parent(x):
            if x not in parent:
                return x
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                return True
            
            return False
        c1 = None
        c2 = None
        for x in range(len(edges)):
            if edges[x][1] in conns:
                c1 = conns[edges[x][1]]
                c2 = [edges[x][0],edges[x][1]]
                break
                
            conns[edges[x][1]] = [edges[x][0],edges[x][1]]
            
            
        for x in range(len(edges)):
            if [edges[x][0],edges[x][1]] == c2:
                continue
                
            if union(edges[x][0]-1,edges[x][1]-1) == False:
                if c1:
                    return c1
                
                return [edges[x][0],edges[x][1]]
            
        return c2
                
            
        
                
                
