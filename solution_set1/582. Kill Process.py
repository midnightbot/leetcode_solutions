##ss
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        edges = {}
        
        for x in range(len(ppid)):
            if ppid[x] > 0:
                if ppid[x] in edges:
                    edges[ppid[x]].add(pid[x])
                    
                else:
                    edges[ppid[x]] = set()
                    edges[ppid[x]].add(pid[x])
                    
                    
        q = set()
        q.add(kill)
        self.killit(edges,q,kill)
        return q
        
    def killit(self,edges,q,kill):
        
        if kill in edges:
            for y in edges[kill]:
                q.add(y)
                self.killit(edges,q,y)
        
