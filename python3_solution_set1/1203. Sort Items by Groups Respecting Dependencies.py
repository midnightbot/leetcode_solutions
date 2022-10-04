##ss
## 40 mins
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        ## ordering in items
        ## ordering in groups
        ## first thought ; 2 topo sorts (on items, on groups)
        
        ##step1 do topo sort on grps
        ## step2 do topo sort inside grps
        
        ##step3 sorting inside grps
        
        ## Steps followed in solution
        ## step1 : find topological ordering among groups
        ## step2 : find topological ordering among elements of a same group (sorted order)
        
        grps = set() ##just to see how many groups are present
        assgn = defaultdict(list) ## key->group ; value->elements in that group
        for x in range(len(group)):
            
            if group[x] == -1:
                group[x] = m
                m+=1
            assgn[group[x]].append(x)
            grps.add(group[x])
                
                
        grp = {x:[] for x in grps}##contains all the edges from beforeitems that do not have same group, that creating graph helpful for step1 (topo sorting among groups)
        #print(group)
        left = []
        for x in range(len(beforeItems)):
            for y in range(len(beforeItems[x])):
                if group[x] != group[beforeItems[x][y]]:
                    grp[group[beforeItems[x][y]]].append(group[x])
                    
                else:
                    left.append([beforeItems[x][y], x])
                    
        ###################
        def topo_sort(graph): ## function returns topo-sort of given graph
            
            indegree = {x:0 for x in graph}
            visited = set()
            ords = []
            for x in graph:
                for y in graph[x]:
                    indegree[y]+=1
                    
            q = []
            
            for x in indegree:
                if indegree[x] == 0:
                    q.append(x)
                    
            while q:
                node = q.pop(0)
                
                if node not in visited:
                    visited.add(node)
                    ords.append(node)
                    
                    for nei in graph[node]:
                        indegree[nei]-=1
                        
                        if indegree[nei] == 0:
                            q.append(nei)
                            
            return ords
        #######################################
        a = topo_sort(grp)## now we know the ordering of groups
        #print(a)
                
        ##here we have finished ordering among groups
        
        ## starting step2 :  now ordering inside groups
        
        result = []
        
        new_g = {x:[] for x in range(n)} ##contains all the left edges from beforeItems
        
        for x in left:
            new_g[x[0]].append(x[1])
        

        for thisgrp in a:##for each group we need, order of its elements
            temp = assgn[thisgrp] ##temp = [all elements of this group]
            temp = sorted(temp) ##sorting as demanded in question
            send_g = {} ##creating graph for this group
            for elem in temp:
                send_g[elem] = new_g[elem]
                
            thisans = topo_sort(send_g)## finding topo-order for this group
            result+=thisans##appending it to the main result
            
        #print(result)
        return result if len(result) == n else []
                
