class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for x in range(3):
            for y in range(3):
                grid[x][y] = 0 if grid[x][y]=='B' else 1

        for x in range(2):
            for y in range(2):
                sums = 0
                sums+=grid[x][y]
                sums+=grid[x][y+1]
                sums+=grid[x+1][y]
                sums+=grid[x+1][y+1]
                if sums in [0,1,3,4]:
                    return True

        return False
        
