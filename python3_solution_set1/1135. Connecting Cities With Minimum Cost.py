##ss
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        connections = sorted(connections, key = lambda x:x[2])
        
        ##minimum spanning tree
        parent = [-1 for x in range(n+1)]
        grps = [n]
        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                grps[0]-=1
                parent[ys] = xs
                return True
            
            return False
        
        result = 0
        for x in range(len(connections)):
            #print(grps)
            if union(connections[x][0],connections[x][1]):
                result+=connections[x][2]
                
                
            if grps[0] == 1:
                return result
            
                
            
        if grps[0] == 1:
            return result
        
        return -1
