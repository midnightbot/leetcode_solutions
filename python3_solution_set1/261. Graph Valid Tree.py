##ss
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        ##basically see there is no cycle
        
        parent = [-1 for x in range(n)]
        self.grps = n
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
                self.grps-=1
                return True
            
            else:
                return False
            
            
        for x in range(len(edges)):
            if union(edges[x][0],edges[x][1]) == False:## to check if there is any cycle
                return False
            
        return self.grps == 1 ##this is basically to check if the graph is connected
        
