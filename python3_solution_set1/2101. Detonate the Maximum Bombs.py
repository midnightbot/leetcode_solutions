##ss
import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        
        ## kind of bfs, union find
        graph = {x:[] for x in range(len(bombs))}
        
        def intersect(arr1,arr2):
            px = arr1[0]
            py = arr1[1]
            r1 = arr1[2]
            
            qx = arr2[0]
            qy = arr2[1]
            r2 = arr2[2]
            
            if math.sqrt((px-qx)**2 + (py-qy)**2) <= r1:
                return True
            return False
            
            
        for x in range(len(bombs)):
            for y in range(len(bombs)):
                if x!=y:
                    if intersect(bombs[x],bombs[y]): 
                        graph[x].append(y)

        def do_bfs(startnode):
            q = [startnode]
            visited = set()
            visited.add(startnode)
            
            while q:
                top = q.pop(0)
                
                for nei in graph[top]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            
            return len(visited)
        
        ans = 1
        for x in range(len(bombs)):
            ans = max(ans, do_bfs(x))
            
        return ans
    
                    
            
