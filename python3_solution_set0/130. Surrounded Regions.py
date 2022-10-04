class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.n = len(board)
        
        if self.n<=2:
            return
        c= len(board[0])
        if c<=2:
            return
        
        for i in range(self.n):
            for j in range(c):
                if board[i][j] == 'O' and(i==0 or i==self.n-1 or j == 0 or j==c-1):
                    self.dfs(i,j)
                    
        for i in range(self.n):
            for j in range(c):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                    
                elif self.board[i][j] == 'A':
                    self.board[i][j] = 'O'
                    
    def dfs(self,i,j):
        if i>=0 and i<len(self.board) and j>=0 and j<len(self.board[0]) and self.board[i][j] == 'O':
            self.board[i][j] = 'A'
            self.dfs(i+1,j)
            self.dfs(i-1,j)
            self.dfs(i,j+1)
            self.dfs(i,j-1)
            
            
        
