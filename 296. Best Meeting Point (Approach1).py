class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        ans  = float('inf')
        
        friends = []
        ans1 = []
        ans2 = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    friends.append((x,y))
                
                    
                    
        for x in range(len(grid)):
            temp = 0
            for z in range(len(friends)):
                temp+= (abs(x-friends[z][0]))
            ans1.append(temp)   
                
        for y in range(len(grid[0])):
            temp = 0
            for z in range(len(friends)):
                temp+=(abs(y-friends[z][1]))
            ans2.append(temp)   
                
        return min(ans1) + min(ans2)
                    
        
