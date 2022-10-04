##ss

## 26 mins
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ##MST
        ##critical - cannot be deleted
        ##pseudocritical - can be deleted
        
        for x in range(len(edges)):
            edges[x].append(x)
            
        edges = sorted(edges, key = lambda x:x[2])
        #print(edges)
        
        ##critical edge - deleting that edge will increase MST cost, or not build a MST
        ##pseduo-critical - may or may not belong to MST (how to find this? Include this edge in MST and the find MST cost and if thismstcost == minmstcost it is pseudo critical)
        
        critical = []
        pseudo_critical = []
        
        parent = [-1 for x in range(n)]
        
        ##general union find template
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
        
        grps = n
        cost = 0
        ##finding MST cost
        for x in range(len(edges)):
            if union(edges[x][0],edges[x][1]):
                cost+=edges[x][2]
                grps-=1
                
            if grps == 1:
                break
         
        #print(cost)
        ## finding critical edges
        for x in range(len(edges)):
            new_e = edges[0:x] + edges[x+1:]
            #print(new_e, x)
            parent = [-1 for x in range(n)]
            thiscost = 0
            grps = n
            for y in range(len(new_e)):
                
                if union(new_e[y][0],new_e[y][1]):
                    thiscost+=new_e[y][2]
                    grps-=1
                
                if grps == 1:
                    break
            #print(thiscost,grps)        
            if (thiscost > cost and grps==1) or (grps > 1):
                critical.append(edges[x][3])
                
        ##finding pseudo-critical edges
        for x in range(len(edges)):
            if edges[x][3] not in critical:
                include = edges[x]
                parent = [-1 for x in range(n)]
                parent[include[0]] = include[1]

                new_e = edges[0:x] + edges[x+1:]

                thiscost = include[2]
                grps = n-1
                #print(parent)
                for y in range(len(new_e)):

                    if grps == 1:
                        break

                    if union(new_e[y][0],new_e[y][1]):
                        thiscost+=new_e[y][2]
                        grps-=1


                #print(thiscost, x)        
                if thiscost == cost and grps == 1:
                    pseudo_critical.append(edges[x][3])
                
        #print(cost)
        return [critical, pseudo_critical]
        
            
