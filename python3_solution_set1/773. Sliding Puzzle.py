##ss
import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        if 0 in board[0]:
            x = 0
            y = board[0].index(0)
            
        else:
            x = 1
            y = board[1].index(0)
        #print(x,y)
        q = [[board,0,x,y]]
        
        visited = set()
        
        while q:
            #print(q)
            thisstate = q.pop(0)
            bd = thisstate[0]
            steps = thisstate[1]
            x = thisstate[2]
            y = thisstate[3]
            
            #nb1 = copy.copy(bd)
            if bd == [[1,2,3],[4,5,0]]:
                #print("fina;",bd)
                return steps
            if x-1>=0:
                nb1 = copy.deepcopy(bd)
                nb1[x-1][y],nb1[x][y] = nb1[x][y],nb1[x-1][y]
                if tuple(nb1[0]+nb1[1]) not in visited:
                    visited.add(tuple(nb1[0]+nb1[1]))
                    q.append([nb1,steps+1,x-1,y])
                 
            if x+1 < len(board):
                nb2 = copy.deepcopy(bd)
                nb2[x+1][y],nb2[x][y] = nb2[x][y],nb2[x+1][y]
                if tuple(nb2[0]+nb2[1]) not in visited:
                    visited.add(tuple(nb2[0]+nb2[1]))
                    q.append([nb2,steps+1,x+1,y])
                    
          
            if y-1>=0:
                nb3 = copy.deepcopy(bd)
                nb3[x][y-1],nb3[x][y] = nb3[x][y],nb3[x][y-1]
                if tuple(nb3[0]+nb3[1]) not in visited:
                    visited.add(tuple(nb3[0]+nb3[1]))
                    q.append([nb3,steps+1,x,y-1])
                    
            
            if y+1 < len(board[0]):
                nb4 = copy.deepcopy(bd)
                nb4[x][y+1],nb4[x][y] = nb4[x][y],nb4[x][y+1]
                if tuple(nb4[0]+nb4[1]) not in visited:
                    visited.add(tuple(nb4[0]+nb4[1]))
                    q.append([nb4,steps+1,x,y+1])
                    
        
        
        #print("visited",visited)
        return -1
                
                
                    
            
            
            
            
