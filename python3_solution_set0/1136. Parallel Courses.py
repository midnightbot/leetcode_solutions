##ss
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        sem = 0
        ##simple bfs topological ordering
        ##each time remove nodes with indegree = 0 as they have no prerequisites
        ##update the indegree of all adjacent nodes
        ##keep repeating the process
        indegree = [0 for x in range(n)]
        dicts = {}##containing adj list
        
        for x in range(len(relations)):
            if relations[x][0] in dicts.keys():
                dicts[relations[x][0]].append(relations[x][1])
                
            else:
                dicts[relations[x][0]] = [relations[x][1]]
                
       # print(dicts)
        
        for x in range(len(relations)):
            indegree[relations[x][1]-1]+=1
            
        visited = set()
        queue = []
        
        for x in range(len(indegree)):
            if indegree[x] == 0:
                queue.append(x+1)
                
        if len(queue) == 0:
            return -1
        
        var = True
        #print(dicts)
        while var:
            temps = []
            var = False
            sem+=1
            for x in range(len(queue)):
                #print(visited,queue,indegree,"start")
                node = queue.pop(0)
                #print(node)
                if node not in visited and node in dicts.keys():
                    #print(node,"inside",dicts[node])
                    for adj in dicts[node]:
                        
                        indegree[adj-1]-=1
                        
                        if indegree[adj-1] == 0 and (adj) not in visited:
                            var = True
                            temps.append(adj)

                visited.add(node)
            #print(visited,queue,indegree,"end",temps)
            queue = temps
        
        #print(visited)
        if len(visited) < n:
            return -1
        
        return sem
        #print(indegree)
