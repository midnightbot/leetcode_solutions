##ss
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == ".":
                    ans = self.validate(board,x,y)
                    if ans == False:
                        return False
                    
        return True
        
        
        
    def validate(self,board,x,y):
        
        ##row check
        rowcheck = []
        for col in range(len(board[0])):
            if board[x][col]!="." and board[x][col] not in rowcheck:
                rowcheck.append(board[x][col])
                
            elif board[x][col]!="." and board[x][col] in rowcheck:
                return False
            
            
            
        ##column check
        colcheck = []
        
        for row in range(len(board)):
            if board[row][y]!="." and board[row][y] not in colcheck:
                colcheck.append(board[row][y])
                
            elif board[row][y]!="." and board[row][y] in colcheck:
                return False
            
        ##ninesquarecheck
        neig = []
        sq = -1
        if x <=2 and y<=2:
            sq = 1
            return self.squarecheck(board,0,3,0,3)
        elif x<=2 and y<=5 and y>2:
            sq = 2
            return self.squarecheck(board,0,3,3,6)
            
        elif x<=2 and y>5:
            sq = 3
            return self.squarecheck(board,0,3,6,9)
            
        elif x>=3 and x<=5 and y<=2:
            sq = 4
            return self.squarecheck(board,3,6,0,3)
            
        elif x>=3 and x<=5 and y<=5 and y>2:
            sq = 5
            return self.squarecheck(board,3,6,3,6)
            
        elif x>=3 and x<=5 and y>5:
            sq = 6
            return self.squarecheck(board,3,6,6,9)
            
        elif x>5 and y<=2:
            sq = 7
            return self.squarecheck(board,6,9,0,3)
            
        elif x>5 and y>2 and y<=5:
            sq = 8
            return self.squarecheck(board,6,9,3,6)
        else:
            sq = 9
            return self.squarecheck(board,6,9,6,9)
            
        
            
    def squarecheck(self,board,rowstart,rowend,colstart,colend):
        
        visited = []
        
        for x in range(rowstart,rowend):
            for y in range(colstart,colend):
                if board[x][y]!="." and board[x][y] not in visited:
                    visited.append(board[x][y])
                    
                elif board[x][y]!="." and board[x][y] in visited:
                    return False
                
        return True
        
