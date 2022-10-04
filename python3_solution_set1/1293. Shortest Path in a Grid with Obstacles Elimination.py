##ss
##simple 3-D bfs
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        if grid == [[0]]:
            return 0
        visited = set()
        ans = float('inf')
        queue = [(0,0,k,0)]
        visited.add((0,0,k))
        if k >= len(grid) + len(grid[0]) - 2:
            return len(grid) + len(grid[0]) - 2
        while queue:
            #print(ans)
            
            for x in range(len(queue)):
                node = queue.pop(0)
                #visited.add(node)
                
                if node[2] >=0 and [node[0],node[1]]!=[len(grid)-1,len(grid[0])-1]:
                    ##up
                    if node[0] - 1 >=0 and grid[node[0]-1][node[1]] == 0 and (node[0]-1,node[1],node[2]) not in visited:
                        queue.append((node[0]-1,node[1],node[2],node[3]+1))
                        visited.add((node[0]-1,node[1],node[2]))
                        if [node[0]-1,node[1]] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1


                    elif node[0] - 1 >=0 and grid[node[0]-1][node[1]] == 1 and (node[0]-1,node[1],node[2]-1) not in visited:
                        queue.append((node[0]-1,node[1],node[2]-1,node[3]+1))
                        visited.add((node[0]-1,node[1],node[2]-1))
                        
                        if node[2]-1>=0 and [node[0]-1,node[1]] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1


                    ##down
                    if node[0] + 1 < len(grid) and grid[node[0]+1][node[1]] == 0 and (node[0]+1,node[1],node[2]) not in visited:
                        queue.append((node[0]+1,node[1],node[2],node[3]+1))
                        visited.add((node[0]+1,node[1],node[2]))
                        
                        if [node[0]+1,node[1]] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1
                        
                        


                    elif node[0] + 1 < len(grid) and grid[node[0]+1][node[1]] == 1 and (node[0]+1,node[1],node[2]-1) not in visited:
                        queue.append((node[0]+1,node[1],node[2]-1,node[3]+1))
                        visited.add((node[0]+1,node[1],node[2]-1))
                        
                        if node[2]-1>=0 and  [node[0]+1,node[1]] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1



                    ##left
                    if node[1]-1>=0 and grid[node[0]][node[1]-1]==0 and (node[0],node[1]-1,node[2]) not in visited:
                        queue.append((node[0],node[1]-1,node[2],node[3]+1))
                        visited.add((node[0],node[1]-1,node[2]))
                        if [node[0],node[1]-1] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1

                    elif node[1]-1>=0 and grid[node[0]][node[1]-1]==1 and (node[0],node[1]-1,node[2]-1) not in visited:
                        queue.append((node[0],node[1]-1,node[2]-1,node[3]+1))
                        visited.add((node[0],node[1]-1,node[2]-1))
                        
                        if node[2]-1>=0 and [node[0],node[1]-1] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1


                    ##right
                    if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1]==0 and (node[0],node[1]+1,node[2]) not in visited:
                        queue.append((node[0],node[1]+1,node[2],node[3]+1))
                        visited.add((node[0],node[1]+1,node[2]))
                        if [node[0],node[1]+1] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1


                    elif node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1]==1 and (node[0],node[1]+1,node[2]-1) not in visited:
                        queue.append((node[0],node[1]+1,node[2]-1,node[3]+1))
                        visited.add((node[0],node[1]+1,node[2]-1))
                        
                        if node[2]-1>=0 and [node[0],node[1]+1] == [len(grid)-1,len(grid[0])-1]:
                            return node[3]+1
                        
                        
                
                    
        return -1
                    
                    
                    
                
                
        
        
