##ss
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        #grid = [[" " for x in range(3)] for y in range(3)]
        self.xcount = 0
        self.ocount = 0
        return self.movescheck(board) and self.winnercheck(board)
        
        
    def movescheck(self,board):
        
        
        
        for x in range(len(board)):
            self.xcount+=board[x].count('X')
            self.ocount+=board[x].count('O')
            
            
        if self.xcount == 0 and self.ocount > 0 or self.ocount > self.xcount:
            return False
        
        return abs(self.xcount - self.ocount) <= 1
    
    
    #def winconditioncheck(self,board):
        
        
    def winnercheck(self,board):
        
        xwin = 0
        ywin = 0
        
        for x in range(len(board)): ## row check
            if board[x] == "XXX":
                xwin+=1
                
            elif board[x] == "OOO":
                ywin+=1
                
             
        ##column check
        if board[0][0]+board[1][0] + board[2][0] == "XXX":
            xwin+=1
            
        elif board[0][0] + board[1][0] + board[2][0] == "OOO":
            ywin+=1
            
        if board[0][1]+board[1][1] + board[2][1] == "XXX":
            xwin+=1
            
        elif board[0][1] + board[1][1] + board[2][1] == "OOO":
            ywin+=1
            
            
        if board[0][2]+board[1][2] + board[2][2] == "XXX":
            xwin+=1
            
        elif board[0][2] + board[1][2] + board[2][2] == "OOO":
            ywin+=1
            
            
        ##diagonal check
        
        if board[0][0]+board[1][1] + board[2][2] == "XXX":
            xwin+=1
            
        elif board[0][0] + board[1][1] + board[2][2] == "OOO":
            ywin+=1
            
            
            
        if board[2][0]+board[1][1] + board[0][2] == "XXX":
            xwin+=1
            
        elif board[2][0] + board[1][1] + board[0][2] == "OOO":
            ywin+=1
            
          
        #print(xwin,ywin)
        return (xwin>=1 and ywin==0 and self.xcount - self.ocount == 1) or (xwin==0 and ywin >= 1 and self.ocount - self.xcount == 0) or (xwin==0 and ywin ==0)
            
