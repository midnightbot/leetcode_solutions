##ss
##Solution 1(Simple BFS)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        ans = []
        pos = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "*":
                    pos.append(x)
                    pos.append(y)
                    break
                    
        queue = [pos]
        steps = 0
        while queue:
            temp = set()
            steps+=1
            for x in range(len(queue)):
                node = queue.pop()
                
                if grid[node[0]][node[1]] == "#":
                    return steps-1
                if node[0]-1>=0 and (grid[node[0]-1][node[1]] == "O" or grid[node[0]-1][node[1]]=="#"):
                    #temp.append([node[0]-1,node[1]])
                    temp.add(tuple((node[0]-1,node[1])))
                    
                if node[0] + 1 < len(grid) and (grid[node[0]+1][node[1]] == "O" or grid[node[0]+1][node[1]] == "#"):
                    #temp.append([node[0]+1,node[1]])
                    temp.add(tuple((node[0]+1,node[1])))
                    
                if node[1]-1>=0 and (grid[node[0]][node[1]-1] == "O" or grid[node[0]][node[1]-1]=="#"):
                    #temp.append([node[0],node[1]-1])
                    temp.add(tuple((node[0],node[1]-1)))
                    
                if node[1]+1 < len(grid[0]) and (grid[node[0]][node[1]+1] == "O" or grid[node[0]][node[1]+1]=="#"):
                    #temp.append([node[0],node[1]+1])
                    temp.add(tuple((node[0],node[1]+1)))
                    
            grid[node[0]][node[1]] = "X"
            queue = temp
            temp = set()
            
        return -1
        
