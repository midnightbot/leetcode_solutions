##ss
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        ##answers = no of groups
        ##count extra edges
        ## if extra cables > no of groups return -1
        
        parent = [-1 for x in range(n)]
        count = {'groups':n, 'extra':0}
        def find_parent(x):
            if parent[x] == -1:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[min(xs,ys)] = max(xs,ys)
                count['groups']-=1
                return True
            
            else:
                count['extra']+=1
                
                
        for x in range(len(connections)):
            union(connections[x][0],connections[x][1])
            
        req_cables = count['groups'] - 1
        
        if req_cables > count['extra']:
            return -1
        return req_cables
        
