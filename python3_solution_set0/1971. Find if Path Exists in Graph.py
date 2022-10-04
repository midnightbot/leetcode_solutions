##ss
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        ##path from start to end
        dicts = {}
        
        for x in range(len(edges)):
            if edges[x][0] in dicts.keys():
                dicts[edges[x][0]].append(edges[x][1])
                
            else:
                dicts[edges[x][0]] = [edges[x][1]]
                
                
            if edges[x][1] in dicts.keys():
                dicts[edges[x][1]].append(edges[x][0])
                
            else:
                dicts[edges[x][1]] = [edges[x][0]]
                
        #print(dicts)
        
        queue = set()
        queue.add(start)
        visited = set()
        
        while queue:
            for x in range(len(queue)):
                node = queue.pop()
                if node == end:
                    return True
                if node not in visited:
                    visited.add(node)
                    for y in range(len(dicts[node])):
                        queue.add(dicts[node][y])
                        
        return False
        
