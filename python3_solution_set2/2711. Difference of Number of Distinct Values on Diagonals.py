class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans = [[0 for x in range(len(grid[0]))]for y in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                s1 = set()
                s2 = set()
                
                x1 = x+1
                y1 = y+1
                while x1<m and y1<n:
                    s1.add(grid[x1][y1])
                    x1+=1
                    y1+=1
                    
                x1 = x-1
                y1 = y-1
                while x1>=0 and y1>=0:
                    s2.add(grid[x1][y1])
                    x1-=1
                    y1-=1
                ans[x][y] = abs(len(s1) - len(s2))
        
        
        return ans
