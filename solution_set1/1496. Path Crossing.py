##ss
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        visited = set()
        visited.add((0,0))
        #print(visited)
        curr = [0,0]
        for x in range(len(path)):
            
            if path[x] == 'N':
                curr = [curr[0]+1,curr[1]]
                
            elif path[x] == 'S':
                curr = [curr[0]-1,curr[1]]
                
            elif path[x] == 'E':
                curr = [curr[0],curr[1]+1]
                
            else:
                curr = [curr[0],curr[1]-1]
                
            if (curr[0],curr[1]) in visited:
                return True
            visited.add((curr[0],curr[1]))
            
        return False
        
