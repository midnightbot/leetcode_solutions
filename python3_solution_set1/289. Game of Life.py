##ss
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = [board[x][y],-1]
                
        for x in range(len(board)):
            for y in range(len(board[0])):
                t1,t2 = self.find_neigh(board,x,y)
                
                if board[x][y][0] == 1:
                    if t1<2:
                        board[x][y][1] = 0
                        
                    elif t1==2 or t1==3:
                        board[x][y][1] = 1
                        
                    elif t1>3:
                        board[x][y][1] = 0
                        
                else:
                    if t1 == 3:
                        board[x][y][1] = 1
                    else:
                        board[x][y][1] = 0
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = board[x][y][1]
                
    def find_neigh(self,board,x,y):
        dead_nei = 0
        live_nei = 0
        
        if x-1>=0 and board[x-1][y][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
            
        if x+1 < len(board) and board[x+1][y][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
        
        if y-1>=0 and board[x][y-1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        if y+1 < len(board[0]) and board[x][y+1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        if x-1>=0 and y-1>=0 and board[x-1][y-1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        if x-1>=0 and y+1<len(board[0]) and board[x-1][y+1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        if x+1 < len(board) and y-1>=0 and board[x+1][y-1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        if x+1<len(board) and y+1<len(board[0]) and board[x+1][y+1][0] == 1:
            live_nei+=1
        else:
            dead_nei+=1
            
        return live_nei,dead_nei
        
