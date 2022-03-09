##ss
class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        
        graph = {}
        paths = set()
        count  = 0 
        for x in range(len(corridors)):
            if corridors[x][0] in graph:
                graph[corridors[x][0]].add(corridors[x][1])
            else:
                graph[corridors[x][0]] = {corridors[x][1]}
                
                
            if corridors[x][1] in graph:
                graph[corridors[x][1]].add(corridors[x][0])
                
            else:
                graph[corridors[x][1]] = {corridors[x][0]}

                
        ##try every node to be in cycle and find cycle
        

        for x in range(1,n+1):
            if x in graph:
                for y in graph[x]:
                    if y > x and y in graph:
                        for z in graph[y]:
                            if z > x and z in graph[x]:
                                count+=1
        
        return count//2           
        #return len(paths)
                            
            
