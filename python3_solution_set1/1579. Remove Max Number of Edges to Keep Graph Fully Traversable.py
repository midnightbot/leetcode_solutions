##ss
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        
        ##cover type3 first and then type1 and type2
        
        parent = [-1 for x in range(n+1)]
        grps = {1:[],2:[],3:[]}
        type3edges = 0
        type1edges = 0
        type2edges = 0
        splits = n
        for x in range(len(edges)):
            grps[edges[x][0]].append([edges[x][1],edges[x][2]])
            
        
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
                return True
            return False
        
        
        for x in grps[3]:
            if union(x[0],x[1]) == True:
                type3edges+=1
                splits-=1
            if splits == 1:
                break
                
        if splits == 1:
            return len(edges) - type3edges
                
        parent_og = copy.deepcopy(parent)
        split_og = copy.deepcopy(splits)
        
        for x in grps[1]:
            
                
            if union(x[0],x[1]) == True:
                type1edges+=1
                splits-=1
                
            if splits == 1:
                break
            
        #print(type1edges,parent)
        parent = parent_og
        splits = split_og
        #print(split)
        
        for x in grps[2]:
            
                
            if union(x[0],x[1]) == True:
                type2edges+=1
                splits-=1
                
            if splits == 1:
                break
                
        #print(type3edges,type1edges,type2edges)
        if splits == 1:
            return len(edges) - type3edges - type2edges - type1edges
        
        return -1
