##ss
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = [[0 for x in range(3)] for y in range(3)]
        for x in range(len(moves)):
            if x%2==0:
                grid[moves[x][0]][moves[x][1]] = "X"
                
            else:
                grid[moves[x][0]][moves[x][1]] = "O"
                
            if self.checkwinner(grid)=="X":
                
                return "A"
            
            elif self.checkwinner(grid) == "O":
                return "B"
            
            
        if len(moves) < 9:
            return "Pending"
        
        else:
            return "Draw"
                
        
        
        
        
    def checkwinner(self,grid):
        player1 = ['X','X','X']
        player2 = ['O','O','O']
        
        for x in range(len(grid)): ##row check
            if grid[x] == player1:
                return "X"
            
            elif grid[x] == player2:
                return "O"
            
            
        if grid[0][0] == grid[1][0] == grid[2][0] == "X": ##column check
            return "X"
        
        elif grid[0][0] == grid[1][0] == grid[2][0] == "O":
            return "O"
            
        elif grid[0][1] == grid[1][1] == grid[2][1] == "X":
            return "X"
        
        elif grid[0][1] == grid[1][1] == grid[2][1] == "O":
            return "O"
        elif grid[0][2] == grid[1][2] == grid[2][2] == "X":
            return "X"
        elif grid[0][2] == grid[1][2] == grid[2][2] == "O":
            return "O"
            
            
        elif grid[0][0] == grid[1][1] == grid[2][2] == "X":
            return "X"
        elif grid[0][0] == grid[1][1] == grid[2][2] == "O":
            return "O"
        
        elif grid[0][2] == grid[1][1] == grid[2][0] == "X":
            return "X"
        elif grid[0][2] == grid[1][1] == grid[2][0] == "O":
            return "O"
        
        
        return -1
