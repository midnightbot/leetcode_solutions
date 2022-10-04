##ss
## Simple BFS/DFS 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                
                if grid[x][y] == 1:
                    queue = set()
                    queue.add(tuple((x,y)))
                    
                    temp = set()
                    while queue:
                        #print(queue)
                        #print(grid)
                        for z in range(len(queue)):
                            node = queue.pop()
                            c=0
                            grid[node[0]][node[1]] = -1

                            if node[0]-1>=0 and grid[node[0]-1][node[1]] == 1:
                                c+=1
                                temp.add(tuple((node[0]-1,node[1])))
                            elif node[0]-1>=0 and grid[node[0]-1][node[1]] == -1:
                                c+=1

                            if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                                c+=1
                                temp.add(tuple((node[0]+1,node[1])))
                            elif node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == -1:
                                c+=1


                            if node[1] - 1 >=0 and grid[node[0]][node[1]-1] == 1:
                                c+=1
                                temp.add(tuple((node[0],node[1]-1)))
                            elif node[1] - 1 >=0 and grid[node[0]][node[1]-1] == -1:
                                c+=1

                            if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                                c+=1
                                temp.add(tuple((node[0],node[1]+1)))
                            elif node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == -1:
                                c+=1
                                
                            ans+=4 - c
                            #print(ans)
                        queue |= temp
                        temp = set()
                        
                    break
                    
        return ans
                        
        
                        
        
