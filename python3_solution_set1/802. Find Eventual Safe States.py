##ss
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        ## terminal node, outgoing = 0
        ## safe-node, evry path starting from this node leads to terminal node
        
        ## simple -> just reverse graph and do topo sort
        
       
      
        g = [[] for x in range(len(graph))]
        
        incoming = {x:0 for x in range(len(graph))}
        
        for x in range(len(graph)):
            
            if len(graph[x])!=0:
                for z in graph[x]:
                    g[z].append(x)
                    incoming[x]+=1
                
        #print(g,incoming)
            
        q = []
        for x in incoming:
            if incoming[x] == 0:
                q.append(x)
                
        safe = set()
        while q:
            top = q.pop(0)
            safe.add(top)
            for nei in g[top]:
                incoming[nei]-=1
                
                if incoming[nei] == 0:
                    q.append(nei)
        
        return sorted(safe)
