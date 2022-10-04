##ss
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ##fully connected and no cycle
        
        
        ##when adding edges if both the points of edge already have same parent, adding edge between them will create a cycle
        ##hence whenever edges[x][0] and edges[x][1] have same parent that edge will be answer
        parent = [-1 for x in range(len(edges)+1)]
        grps = [len(edges)]
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
                grps[0]-=1
                return True
                
            return False
                
                
        for x in range(len(edges)):
           
            if union(edges[x][0],edges[x][1]) == False:
                return edges[x]
            #print(grps[0])
            
                
                
        
        
