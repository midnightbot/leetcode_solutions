##ss
##basic union find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = [n]
        
        parent = [-1 for x in range(n)]
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                count[0]-=1
                
                
        for x in range(len(edges)):
            union(edges[x][0],edges[x][1])
            
        return count[0]
        
        
