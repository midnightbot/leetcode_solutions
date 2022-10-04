##Solution 1 (Time Limit Exceeded   Passes all cases except one case)
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        ans = set()
        
        children = {}
        
        for x in range(len(pid)):
            temp = []
            for y in range(len(ppid)):
                if pid[x] == ppid[y]:
                    temp.append(pid[y])
                    
            children[pid[x]] = temp
        #print(children)
        ##children, (key->parent) (value is a array representing all its children)
        visited = {}
        queue = []
        queue = children[kill]
        visited[kill] = 1
        while queue:
            temp = set()
            for x in range(len(queue)):
                node = queue.pop()
                
                if node not in visited.keys():
                    visited[node] = 1
                    vals = children[node]
                    for z in range(len(vals)):
                        if vals[z] not in visited.keys():
                            temp |= set(vals[z])
                    #temp |= set(children[node])
                
            queue = temp
            temp = set
            
        return visited.keys()
        
        
        
