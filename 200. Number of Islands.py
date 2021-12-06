##ss
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ##simple bfs/dfs problem category
        
        count = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                #print(x,y,grid[x][y])
                #print(grid)
                #print(grid[x][y] == "1", grid[x][y])
                if grid[x][y] == "1":
                    queue = set()
                    count+=1
                    queue.add(tuple((x,y)))
                    
                    temp = set()
                    
                    while len(queue)!=0:
                        for z in range(len(queue)):
                            node = queue.pop()
                            grid[node[0]][node[1]] = -1
                            if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == "1":
                                #print(node[0]+1,node[1])
                                temp.add(tuple((node[0]+1,node[1])))

                            if node[0]-1 >=0  and grid[node[0]-1][node[1]] == "1":
                                #print(node[0]-1,node[1])
                                temp.add(tuple((node[0]-1,node[1])))

                            if node[1]-1 >=0 and grid[node[0]][node[1]-1] == "1":
                                #print(node[0],node[1]-1)
                                temp.add(tuple((node[0],node[1]-1)))

                            if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == "1":
                                #print(node[0],node[1]+1)
                                temp.add(tuple((node[0],node[1]+1)))

                        #print(temp)   
                        #print(grid)
                        #print(grid)
                        #print(queue)
                        queue |= temp
                        #print(queue)
                        temp = set()
                     
                        
                        
        return count
                        
                   
                    
        
