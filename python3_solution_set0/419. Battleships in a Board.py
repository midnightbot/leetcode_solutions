##ss
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        count = 0
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "X":
                    self.find_ship(x,y,board)
                    count+=1
                
        return count
    
    
    def find_ship(self,x,y,board): ## do simple bfs
        ##as ships will be sepearted by atleast one gap we need not worry ship is vertical or horizontal
        ##is ship is vertical, there will be gap in horizontal direction and bfs will noe move forward in that direction. Similrar is the case when ship is horizontal
        queue = [(x,y)]
        
        while queue:
            node = queue.pop(0)
            
            if node[0] -1 >=0 and board[node[0]-1][node[1]] == "X":
                queue.append((node[0]-1,node[1]))
                board[node[0]-1][node[1]] = "."
                
                
            if node[0] + 1 < len(board) and board[node[0]+1][node[1]] == "X":
                queue.append((node[0]+1,node[1]))
                board[node[0]+1][node[1]] = "."
                
                
            if node[1] - 1>=0 and board[node[0]][node[1]-1] == "X":
                queue.append((node[0],node[1]-1))
                board[node[0]][node[1]-1] = "."
                
            if node[1] + 1 < len(board[0]) and board[node[0]][node[1]+1] == "X":
                queue.append((node[0],node[1]+1))
                board[node[0]][node[1]+1] = "."
                
                
            board[node[0]][node[1]] = "."
            
        
