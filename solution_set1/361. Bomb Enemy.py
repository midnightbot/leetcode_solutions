##ss
##kind of prefix sum
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        #left,right,top,bottom
        ##one bomb try all empty points -> solution1
        
        
        rl = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        rr = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        cu = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        cd = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        
        for x in range(len(grid)):
            if grid[x][0] == "E":
                rl[x][0] = 1
        
        if len(grid[0]) > 1:
            for x in range(len(grid)):
                for y in range(1,len(grid[0])):
                    if grid[x][y] == 'W':
                        rl[x][y] = 0
                    elif grid[x][y] == 'E':
                        rl[x][y] = 1 + rl[x][y-1]

                    elif grid[x][y] == '0':
                        rl[x][y] = rl[x][y-1]
                    
        
        for x in range(len(grid)):
            if grid[x][-1] == "E":
                rr[x][-1] = 1
           
        if len(grid[0]) > 1:
            for x in range(len(grid)):
                for y in range(len(grid[0])-2,-1,-1):
                    #print(x,y)
                    if grid[x][y] == 'W':
                        rr[x][y] = 0

                    elif grid[x][y] == 'E':
                        rr[x][y] = 1 + rr[x][y+1]

                    elif grid[x][y] == '0':
                        rr[x][y] = rr[x][y+1]
                    
        ##rl,rr -> done
        
        for x in range(len(grid[0])):
            if grid[0][x] == 'E':
                cu[0][x] = 1
                
        if len(grid) > 1:
            for x in range(len(grid[0])):
                for y in range(1, len(grid)):
                    if grid[y][x] == 'W':
                        cu[y][x] = 0

                    elif grid[y][x] == 'E':
                        cu[y][x] = 1 + cu[y-1][x]

                    elif grid[y][x] == '0':
                        cu[y][x] = cu[y-1][x]
                    
        for x in range(len(grid[0])):
            if grid[-1][x] == 'E':
                cd[-1][x] = 1
                
        if len(grid) > 1:
            for x in range(len(grid[0])):
                for y in range(len(grid)-2,-1,-1):
                    if grid[y][x] == 'W':
                        cd[y][x] = 0

                    elif grid[y][x] == 'E':
                        cd[y][x] = 1 + cd[y+1][x]

                    elif grid[y][x] == '0':
                        cd[y][x] = cd[y+1][x]
                    
        ans = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '0':
                    ans = max(ans,rl[x][y]+rr[x][y]+cu[x][y]+cd[x][y])
                    
        return ans
                    
