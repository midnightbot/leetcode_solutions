##ss
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        ##simple bfs
        
        q = [start]
        
        options = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            
            node = q.pop(0)
            maze[node[0]][node[1]] = -1
            if node[0] == destination[0] and node[1] == destination[1]:
                return True
            
            
            for opt in options:
                r = node[0] + opt[0]
                c = node[1] + opt[1]
                
                while r>=0 and c>=0 and r<len(maze) and c<len(maze[0]) and maze[r][c] != 1:
                    r+=opt[0]
                    c+=opt[1]
                    
                r-=opt[0]
                c-=opt[1]
                
                if maze[r][c] == 0:
                    q.append([r,c])
                    
        return False
                    
        
