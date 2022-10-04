##ss
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        ##simple bfs topological sort
        ##almost same as 1136. Parallel Courses
        
        times = 0
        indegree = [0 for x in range(n)]
        dicts = {}
        queue = []
        outs = {}
        for x in range(len(relations)):
            if relations[x][0] in dicts.keys():
                dicts[relations[x][0]].append(relations[x][1])
                
            else:
                dicts[relations[x][0]] = [relations[x][1]]
                
                
            if relations[x][1] in outs.keys():
                outs[relations[x][1]].append(relations[x][0])
                
            else:
                outs[relations[x][1]] = [relations[x][0]]
        for x in range(len(relations)):
            indegree[relations[x][1]-1]+=1
            
            
        for x in range(len(indegree)):
            if indegree[x] == 0:
                queue.append((x+1,time[x]))

        

        visited = set()
        max_time = 0
        while queue:
            temps = []
            #print(queue)
            #thistime = -float('inf')
            for x in range(len(queue)):
                nodes = queue.pop(0)
                node = nodes[0]
                max_time = max(max_time,nodes[1])
                #print(node)
                #thistime = max(thistime, time[node-1])
                if node not in visited and node in dicts.keys():
                    #print(node,"inside",dicts[node])
                    for adj in dicts[node]:
                        
                        indegree[adj-1]-=1
                        
                        if indegree[adj-1] == 0 and (adj) not in visited:
                            var = True
                            add_time = 0
                            for mx in outs[adj]:
                                add_time = max(add_time, time[mx-1])
                                
                               
                            temps.append((adj,time[adj-1]+add_time))
                            time[adj-1]+=add_time

                visited.add(tuple((node,nodes[1])))
            #times+=thistime
            queue = temps
            
        return max_time
        
