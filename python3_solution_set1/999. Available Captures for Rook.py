##ss
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        for x in range(len(board)):
            print(board[x])
        ans = 0
        var = False
        for x in range(len(board)):
            if var == True:
                break
            for y in range(len(board[0])):
                if board[x][y] == 'R':
                    var = True
                    break
                    
        positions = [x-1,y]
        print(positions)
        ##left, right, top, bottom
        
        if positions[1] > 0:##left
            for x in range(positions[1]-1,-1,-1):
                if board[positions[0]][x] == '.':
                    continue
                    
                else:
                    if board[positions[0]][x] == 'p':
                        ans+=1
                        
                    break
        print(ans,"ans")            
        if positions[1] < len(board[0]):##right
            for x in range(positions[1]+1,len(board[0])):
                #print(x,positions)
                if board[positions[0]][x] == '.':
                    continue
                    
                else:
                    if board[positions[0]][x] == 'p':
                        ans+=1
                        
                    break
        print(ans,"ans")               
        if positions[0] > 0:##up
            for x in range(positions[0]-1,-1,-1):
                #print(x)
                if board[x][positions[1]] == '.':
                    continue
                    
                else:
                    if board[x][positions[1]] == 'p':
                        ans+=1
                        
                    break
        print(ans,"ans")               
        if positions[0] < len(board):##down
            for x in range(positions[0]+1,len(board)):
                if board[x][positions[1]] == '.':
                    continue
                    
                else:
                    if board[x][positions[1]] == 'p':
                        ans+=1
                        
                    break
        print(ans,"ans")              
        return ans
